from rest_framework import serializers
from ..models import OCRRequest


class OCRRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = OCRRequest
        fields = '__all__'
