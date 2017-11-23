from django.utils.translation import ugettext as _
from django.conf.urls import url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title=_('Accounting API'))

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', schema_view),
]
