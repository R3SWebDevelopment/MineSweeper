from rest_framework import viewsets

from .serializers import CompanySerializer, Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['get', 'post']

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return super(CompanyViewSet, self).get_queryset(*args, **kwargs)
        return user.companies.all()
