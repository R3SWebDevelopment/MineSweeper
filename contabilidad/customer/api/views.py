from rest_framework import viewsets
from rest_framework.decorators import detail_route
from .serializers import CompanySerializer, Company
from rest_framework.response import Response
from rest_framework import status
from .permissions import AdminAndCollaboratorPermission
from rest_framework.permissions import IsAuthenticated


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['get', 'post']
    permission_classes = (AdminAndCollaboratorPermission, IsAuthenticated)

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return super(CompanyViewSet, self).get_queryset(*args, **kwargs)
        return user.companies.all()

    @detail_route(methods=['post'])
    def add_collaborators(self, request, pk):
        company = self.get_object()
        return Response({}, status=status.HTTP_403_FORBIDDEN)

