from rest_framework.routers import DefaultRouter
from .views import GameAccessViewSet

router = DefaultRouter()
router.register(r'access', GameAccessViewSet, base_name='access')
urlpatterns = router.urls
