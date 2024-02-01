from rest_framework import routers

from gallery.viewsets import GalleryViewSet

router = routers.SimpleRouter()

router.register(r'gallery', GalleryViewSet, basename='gallery')

urlpatterns = router.urls
