from django.urls import path, include
from .views import ReviewModelViewSet
from mangoreviews import views


urlpatterns = [
    path('api/v1/review/', views.ReviewModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v1/review/<int:pk>/', views.ReviewModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    ]