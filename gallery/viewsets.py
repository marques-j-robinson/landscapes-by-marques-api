from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from gallery.models import Gallery

from gallery.serializers import GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [AllowAny]
