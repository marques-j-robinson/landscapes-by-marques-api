from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from painting.models import Painting

from painting.serializers import PaintingSerializer


class PaintingViewSet(viewsets.ModelViewSet):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer
    permission_classes = [AllowAny]
