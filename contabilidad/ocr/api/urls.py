from rest_framework import routers
from .views import OCRRequestViewSet

router = routers.SimpleRouter()

router.register(r'ocr', OCRRequestViewSet)

urlpatterns = router.urls
