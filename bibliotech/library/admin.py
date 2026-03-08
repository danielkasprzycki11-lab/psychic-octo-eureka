from django.contrib import admin
from .models import Author, Genre, Book, Copy, Reservation


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CopyInline(admin.TabularInline):
    model = Copy
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    list_filter = ('genre', 'author')
    search_fields = ('title', 'author__name')
    inlines = [CopyInline]  # Egzemplarze w tym samym oknie


@admin.register(Copy)
class CopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'status')
    list_filter = ('status',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'copy', 'reserved_at', 'valid_until')
    list_filter = ('reserved_at', 'valid_until')
