from django.urls import path, include
from .views import MangaModelViewSet
from mangocatalog import views


urlpatterns = [
    path('api/v1/manga/', views.MangaModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v1/manga/<int:pk>/', views.MangaModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    ]