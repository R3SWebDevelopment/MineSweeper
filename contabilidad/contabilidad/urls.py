from django.utils.translation import ugettext as _
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views
from django.conf import settings

schema_view = get_swagger_view(title=_('Accounting API'))

urlpatterns = [
    url("^admin/", admin.site.urls),
    # url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/', include('ocr.api.urls', namespace='ocr_api')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^$', schema_view),
    url(r'^avatar/', include('avatar.urls')),
]

if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
