from django.db import models
from crum import get_current_user
from django.contrib.auth.models import User


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