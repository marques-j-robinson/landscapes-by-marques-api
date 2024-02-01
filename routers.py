from rest_framework import routers

from painting.viewsets import PaintingViewSet

router = routers.SimpleRouter()

router.register(r'painting', PaintingViewSet, basename='painting')

urlpatterns = router.urls
