from rest_framework import serializers

from painting.models import Painting


class PaintingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Painting
        fields = ['title', 'description', 'dimensions', 'image', 'published', 'created', 'updated', 'id']
        read_only_fields = ['created', 'updated', 'id']
