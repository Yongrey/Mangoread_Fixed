from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import MangaListSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Manga
from .filters import MangaFilter


class MangaModelViewSet(ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaListSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = MangaFilter
    search_fields = ('title',)
