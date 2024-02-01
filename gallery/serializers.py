from rest_framework import serializers

from gallery.models import Gallery


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ['title', 'description', 'dimensions', 'image', 'published', 'created', 'updated', 'id']
        read_only_fields = ['created', 'updated', 'id']
