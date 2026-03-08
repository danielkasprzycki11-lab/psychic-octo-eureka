from datetime import date, timedelta

from rest_framework import viewsets, permissions, serializers
from .models import Author, Genre, Book, Copy, Reservation
from .serializers import (
    AuthorSerializer,
    GenreSerializer,
    BookSerializer,
    CopySerializer,
    ReservationSerializer,
    ReservationCreateSerializer,
)


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.select_related('author', 'genre').all()
    serializer_class = BookSerializer


class CopyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Copy.objects.select_related('book', 'book__author', 'book__genre').all()
    serializer_class = CopySerializer


class ReservationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reservation.objects.select_related('copy__book').all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ReservationCreateSerializer
        return ReservationSerializer

    def perform_create(self, serializer):
        copy = serializer.validated_data['copy']
        if copy.status != 'available':
            raise serializers.ValidationError('Ten egzemplarz nie jest dostępny.')

        today = date.today()
        valid_until = today + timedelta(days=14)

        reservation = serializer.save(
            user=self.request.user,
            reserved_at=today,
            valid_until=valid_until,
        )

        copy.status = 'reserved'
        copy.save()

        return reservation
