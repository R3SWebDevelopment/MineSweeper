from django.utils.translation import ugettext as _
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views
from django.conf import settings

from users.api.views import FacebookLogin
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_swagger_view(title=_('Django Skeleton'))

urlpatterns = [
    url("^admin/", admin.site.urls),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^users/', include('users.api.urls', namespace='users_api')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^system/', include('utils.api.urls', namespace='system_api')),
    url(r'^mineswipper/', include('mine_swipper.api.urls', namespace='mine_swipper')),
    url(r'^$', schema_view),
    url(r'^avatar/', include('avatar.urls')),
]

if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
