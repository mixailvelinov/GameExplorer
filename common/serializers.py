from rest_framework import serializers
from .models import Platform, Genre


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('platform_name', )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_name', )

