from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from crum import get_current_user
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from datetime import datetime
from celery import uuid

PROCESS_STATUS_NULL = 0
PROCESS_STATUS_QUEUED = 1
PROCESS_STATUS_CANCELED = 2
PROCESS_STATUS_PROGRESS = 3
PROCESS_STATUS_COMPLETED = 4
PROCESS_STATUS_ERROR = 5

##
##                         |---------------------------|
##                         |  |-----------|            ^
##                         |  |           ^            |
##                         |  |           |            |
##                         |  |         ERROR          |
##                         |  |           ^            |
##                         V  V           |            |
## PROCESS FLOW  NULL --> QUEUED --> PROGRESS --> COMPLETED
##                         ^  V            |
##                         |  |            V
##                         |  |-------->CANCELED
##                         |                 v
##                         |-----------------|

PROCESS_STATUS = (
    (PROCESS_STATUS_NULL, _('NULL')),
    (PROCESS_STATUS_QUEUED, _('QUEUED')),
    (PROCESS_STATUS_CANCELED, _('CANCELED')),
    (PROCESS_STATUS_PROGRESS, _('PROGRESS')),
    (PROCESS_STATUS_COMPLETED, _('COMPLETED')),
    (PROCESS_STATUS_ERROR, _('ERROR')),
)

def get_current_user_or_none():
    current_user = get_current_user()
    return None if current_user is None else current_user


class OwnerModelManager(models.Manager):
    def get_queryset(self):
        current_user = get_current_user()
        if current_user is not None and current_user.is_authenticated:
            qs = super().get_queryset(owner=current_user)
            if not current_user.is_staff:
                qs = qs.filter()
            return qs
        return super().get_queryset().none()


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, null=True, default=get_current_user_or_none)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    object = OwnerModelManager()

    class Meta:
        abstract = True


class CeleryProcessable(models.Model):
    process_id = models.UUIDField(null=True)
    process_status = models.IntegerField(null=False, choices=PROCESS_STATUS, default=PROCESS_STATUS_NULL)
    process_started_at = models.DateTimeField(null=True)
    process_updated_at = models.DateTimeField(null=True)
    process_has_error = models.NullBooleanField(default=None)
    process_error_msg = models.TextField(null=True)
    process_log = ArrayField(JSONField())

    @classmethod
    def get_process_method(cls):
        raise Exception(_('Need to define process script'))

    def process_start(self):
        if self.process_status in [PROCESS_STATUS_NULL, PROCESS_STATUS_COMPLETED, PROCESS_STATUS_ERROR,
                                   PROCESS_STATUS_CANCELED]:
            process_method = CeleryProcessable.get_process_method()
            task_id = uuid()
            self.process_status = PROCESS_STATUS_QUEUED
            self.process_started_at = datetime.now()
            self.process_updated_at = None
            self.process_id = task_id
            self.set_process_error_msg()
            self.add_process_log(msg="The process its been set on queue to be processed", start=True)
            self.save()
            process_method.apply_async(id=self.id, task_id=task_id)
        else:
            raise Exception(_("This action is not allowed"))

    def add_process_log(self, msg=None, start=False):
        if msg and msg.strip():
            log = [] if start else self.process_log or []
            log.append({
                "timestamp": datetime.now(),
                "msg": msg
            })

    def set_process_error_msg(self, msg=None):
        self.process_error_msg = msg
        self.process_has_error = None if msg is None else True
        if self.process_has_error:
            self.set_process_status(status=PROCESS_STATUS_ERROR)

    def set_process_status(self, status=None):
        if status is not None:
            if status == PROCESS_STATUS_NULL:
                raise Exception(_('This status is not allowed'))
            if status == PROCESS_STATUS_QUEUED:
                self.process_start()
                return
            if status == PROCESS_STATUS_PROGRESS:
                if self.process_status not in [PROCESS_STATUS_QUEUED]:
                    raise Exception(_('This status is not allowed'))
                self.add_process_log(msg="The process has been started")
            if status == PROCESS_STATUS_CANCELED:
                if self.process_status not in [PROCESS_STATUS_QUEUED, PROCESS_STATUS_PROGRESS]:
                    raise Exception(_('This status is not allowed'))
                self.add_process_log(msg="The process has been canceled")
            if status == PROCESS_STATUS_ERROR:
                if self.process_status not in [PROCESS_STATUS_PROGRESS]:
                    raise Exception(_('This status is not allowed'))
                self.add_process_log(msg="The process has been stopped cause an error")
            if status == PROCESS_STATUS_COMPLETED:
                if self.process_status not in [PROCESS_STATUS_PROGRESS]:
                    raise Exception(_('This status is not allowed'))
                self.add_process_log(msg="The process has been completed")
            self.process_status = status
            self.process_updated_at = datetime.now()
            self.save()
        else:
            raise ValueError(_('No Status parameter provided'))
