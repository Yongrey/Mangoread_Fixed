from rest_framework import serializers
from .models import Manga, Review, Genre, Category
from rest_framework.exceptions import ValidationError


class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = "id title description category year poster genre".split()


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "id text manga stars".split()


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "id name".split()


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id name".split()
