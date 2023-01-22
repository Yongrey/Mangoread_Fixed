from rest_framework import serializers
from .models import Manga, Genre, Category
from rest_framework.exceptions import ValidationError


class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ('id', 'title', 'description', 'category', 'year', 'poster', 'genre')


