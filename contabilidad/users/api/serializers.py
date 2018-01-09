from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer, UserDetailsSerializer
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
        user.first_name = cleaned_data.get('first_name', '')
        user.last_name = cleaned_data.get('last_name', '')
        user.save()
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


class LogInSerializer(LoginSerializer):
    username = serializers.HiddenField(default="")

    def validate(self, attrs):
        attrs.update({
            'username': attrs.get('email', ''),
        })
        return super(LogInSerializer, self).validate(attrs)


class UserSerializer(UserDetailsSerializer):
    notify_by_email = serializers.SerializerMethodField()
    notify_by_sms = serializers.SerializerMethodField()
    mobile_country_code = serializers.SerializerMethodField()
    mobile_number = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'notify_by_email', 'notify_by_sms', 'mobile_country_code',
                  'mobile_number')
        read_only_fields = ('email', )

    def get_notify_by_sms(self, obj, *args, **kwargs):
        try:
            profile = obj.profile
        except:
            profile = None
        return False if profile is None else profile.notify_by_sms

    def get_notify_by_email(self, obj, *args, **kwargs):
        try:
            profile = obj.profile
        except:
            profile = None
        return False if profile is None else profile.notify_by_email

    def get_mobile_country_code(self, obj, *args, **kwargs):
        try:
            profile = obj.profile
        except:
            profile = None
        return '' if profile is None and profile.mobile_number is None \
            else profile.mobile_number.get('country_code', '')

    def get_mobile_number(self, obj, *args, **kwargs):
        try:
            profile = obj.profile
        except:
            profile = None
        return '' if profile is None and profile.mobile_number is None \
            else profile.mobile_number.get('mobile_number', '')
