from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    AuthorViewSet,
    GenreViewSet,
    BookViewSet,
    CopyViewSet,
    ReservationViewSet,
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'books', BookViewSet, basename='book')
router.register(r'copies', CopyViewSet, basename='copy')
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),
]
