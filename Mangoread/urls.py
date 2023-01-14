from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from Mangoread_logic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/manga/', views.MangaModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v1/manga/<int:id>/', views.MangaModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('api/v1/review/', views.ReviewModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v1/review/<int:id>/', views.ReviewModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('api/v1/category/', views.CategoryModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v1/category/<int:id>/', views.CategoryModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('api/v1/genre/', views.GenreModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v1/genre/<int:id>/', views.GenreModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('account/', include('account.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
