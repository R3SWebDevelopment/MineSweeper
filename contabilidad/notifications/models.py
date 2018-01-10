from django.db import models
from django.contrib.postgres.fields import ArrayField


class Notification(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    email = models.BooleanField(default=False)

    email_address = ArrayField(
        models.CharField(max_length=250, null=True)
    )

    email_subject = models.CharField(max_length=250, null=True)
    email_message = models.TextField()
    email_send = models.BooleanField(default=False)
    email_has_error = models.BooleanField(default=False)
    email_response = models.TextField()
    email_error = models.TextField()

    sms = models.BooleanField(default=False)

    mobile_number = ArrayField(
        models.CharField(max_length=20, null=True)
    )

    sms_subject = models.CharField(max_length=250, null=True)
    sms_message = models.TextField()
    sms_send = models.BooleanField(default=False)
    sms_has_error = models.BooleanField(default=False)
    sms_response = models.TextField()
    sms_error = models.TextField()