from rest_framework.response import Response
from .models import Manga, Review, Genre, Category
from .serializers import (CategoryListSerializer, ReviewListSerializer, MangaListSerializer, GenreListSerializer)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .service import MangaFilter
from rest_framework.filters import SearchFilter, OrderingFilter


class MangaModelViewSet(ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaListSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = MangaFilter
    search_fields = ('title',)
    permission_classes = IsAuthenticated


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    permission_classes = IsAuthenticated


class GenreModelViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    permission_classes = IsAuthenticated


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    permission_classes = IsAuthenticated
