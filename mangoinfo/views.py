from rest_framework.response import Response
from .models import Genre, Category
from .serializers import (CategoryListSerializer, GenreListSerializer)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Category, Genre

class GenreModelViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    pagination_class = PageNumberPagination



class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = PageNumberPagination

