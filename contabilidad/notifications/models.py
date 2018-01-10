from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
import boto3
from django.conf import settings

SNS_ENABLED = settings.SNS_ENABLED or False
SNS_ACCESS_KEY = settings.SNS_ACCESS_KEY or None
SNS_SECRET_ACCESS_KEY = settings.SNS_SECRET_ACCESS_KEY or None
SNS_REGION_NAME = settings.SNS_REGION_NAME or None


def is_sms_enable():
    if SNS_ENABLED and SNS_ACCESS_KEY is not None and SNS_SECRET_ACCESS_KEY is not None and SNS_REGION_NAME is not None:
        return True
    return False


class Notification(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    email = models.BooleanField(default=False)

    email_address = ArrayField(
        models.CharField(max_length=250, null=True)
    )

    email_subject = models.CharField(max_length=250, null=True)
    email_message = models.TextField()
    email_send = JSONField()
    email_has_error = JSONField()
    email_response = JSONField()
    email_error = JSONField()

    sms = models.BooleanField(default=False)

    mobile_number = ArrayField(
        models.CharField(max_length=20, null=True)
    )

    sms_subject = models.CharField(max_length=250, null=True)
    sms_message = models.TextField()
    sms_send = JSONField()
    sms_has_error = JSONField()
    sms_response = JSONField()
    sms_error = models.TextField()

    process_begins = models.DateTimeField(null=True)
    process_began = models.BooleanField(default=False)

    process_ends = models.DateTimeField(null=True)
    process_end = models.BooleanField(default=False)

    @classmethod
    def notify(cls, users, email_subject, email_message, sms_subject, sms_message, sms_override=False,
               email_override=False):
        numbers = []
        mails = []

        if not sms_override:

            if is_sms_enable() and users is not None:
                numbers_list = list(users.objects.filter(profile__notify_by_email=True).
                                    values_list('profile__mobile_number', flat=True))

                for num in numbers_list:
                    number = "{}{}".format(num.get('country_code', ''), num.get('number', ''))
                    if number.strip():
                        numbers.append(number)

        if not email_override:
            mails = list(users.objects.filter(profile__notify_by_sms=True).values_list('email', flat=True))

        if len(numbers) > 0 or len(mails) > 0:
            send_mail = len(mails) > 0
            send_sms = len(numbers) > 0
            notification = cls.objects.create(email=send_mail, sms=send_sms, email_subject=email_subject,
                                              email_message=email_message, sms_subject=sms_subject,
                                              sms_message=sms_message)
            notification.email_address = mails
            notification.mobile_number = numbers
            notification.save()

    def _send_email(self):
        pass

    def _send_sms(self):
        try:
            aws_access_key_id = None
            aws_secret_access_key = None
            region_name = None

            client = boto3.client('sns', aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key, region_name=region_name)

            response = client.publish(PhoneNumber='+528110713920', Message='Testing TEXT', Subject='OTRA')
        except Exception as e:
            pass
