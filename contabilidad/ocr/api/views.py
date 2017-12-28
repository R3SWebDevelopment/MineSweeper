from rest_framework import viewsets

from .serializers import OCRRequestSerializer, OCRRequest


class OCRRequestViewSet(viewsets.ModelViewSet):
    queryset = OCRRequest.objects.all()
    serializer_class = OCRRequestSerializer
    http_method_names = ['get', 'post']
