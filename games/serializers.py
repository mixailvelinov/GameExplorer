from rest_framework import serializers

from common.models import Platform, Genre
from common.serializers import PlatformSerializer, GenreSerializer
from .models import Game, Review


class GameSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Game
        fields = '__all__'

    def create(self, validated_data):
        platforms_data = validated_data.pop('platform', [])
        genres_data = validated_data.pop('genre', [])

        #game object
        game = Game.objects.create(**validated_data)

        #platforms
        platforms = []
        for platform_data in platforms_data:
            platform, created = Platform.objects.get_or_create(platform_name=platform_data['platform_name'])
            platforms.append(platform)
        game.platform.set(platforms)

        #genres
        genres = []
        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(genre_name=genre_data['genre_name'])
            genres.append(genre)
        game.genre.set(genres)

        return game

    def update(self, instance, validated_data):
        platforms_data = validated_data.pop('platform', None)
        if platforms_data:
            instance.platform.clear()
            for platform_data in platforms_data:
                platform_name = platform_data['platform_name']
                platform = Platform.objects.filter(platform_name=platform_name).first()
                if platform:
                    instance.platform.add(platform)
                else:
                    platform = Platform.objects.create(platform_name=platform_name)
                    instance.platform.add(platform)

        genres_data = validated_data.pop('genre', None)
        if genres_data:
            instance.genre.clear()
            for genre_data in genres_data:
                genre_name = genre_data['genre_name']
                genre = Genre.objects.filter(genre_name=genre_name).first()
                if genre:
                    instance.genre.add(genre)
                else:
                    genre = Genre.objects.create(genre_name=genre_name)
                    instance.genre.add(genre)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating', 'review']

