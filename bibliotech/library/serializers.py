from rest_framework import serializers
from .models import Author, Genre, Book, Copy, Reservation


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'description',
            'publication_date',
            'author',
            'genre',
        ]


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Copy
        fields = ['id', 'book', 'status']


class ReservationSerializer(serializers.ModelSerializer):
    copy = CopySerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'copy', 'reserved_at', 'valid_until']

class ReservationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['copy']  # użytkownika i daty ustawimy w widoku
