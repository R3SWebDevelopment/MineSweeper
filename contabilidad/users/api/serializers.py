from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User
from users.models import Profile


class RegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    country_phone_code = serializers.CharField(required=True, write_only=True, max_length=4)
    mobile_number = serializers.CharField(required=True, write_only=True, max_length=10)
    username = serializers.HiddenField(default="SAME")

    class Meta:
        model = User
        fields = '__all__'

    def save(self, request, *args, **kwargs):
        user = super(RegistrationSerializer, self).save(request)
        cleaned_data = self.get_cleaned_data()
        mobile_number = {
            "country_code": "",
            "number": ""
        }
        profile = Profile.objects.create(user=user, mobile_number=mobile_number, notify_by_email=True,
                                         notify_by_sms=True)
        return user

    def get_cleaned_data(self):
        cleaned_data = super(RegistrationSerializer, self).get_cleaned_data()
        cleaned_data.update({
            "username": cleaned_data.get('email', ''),
            "first_name": self.validated_data.get('first_name', ''),
            "last_name": self.validated_data.get('last_name', ''),
            "country_phone_code": self.validated_data.get('country_phone_code', ''),
            "mobile_number": self.validated_data.get('mobile_number', ''),
        })
        return cleaned_data
