from django.urls import path, include
from .views import CategoryModelViewSet, GenreModelViewSet
from  mangoinfo import views

urlpatterns = [
path('api/v1/category/', views.CategoryModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v1/category/<int:pk>/', views.CategoryModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('api/v1/genre/', views.GenreModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v1/genre/<int:pk>/', views.GenreModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    ]