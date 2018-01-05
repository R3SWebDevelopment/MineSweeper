from rest_framework import serializers
from rest_framework import fields
from ..models import Company
from utils.api.serializers import UserSerializer


class CompanySerializer(serializers.ModelSerializer):
    collaborators = UserSerializer(many=True)

    class Meta:
        model = Company
        fields = ('full_name', 'rfc', 'address', 'collaborators')