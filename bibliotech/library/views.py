from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Book, Genre, Author, Copy

def book_list(request):
    books = Book.objects.select_related('author', 'genre').all()
    genre_id = request.GET.get('genre')
    author_id = request.GET.get('author')
    query = request.GET.get('q')

    if genre_id:
        books = books.filter(genre_id=genre_id)
    if author_id:
        books = books.filter(author_id=author_id)
    if query:
        books = books.filter(title__icontains=query)

    context = {
        'books': books,
        'genres': Genre.objects.all(),
        'authors': Author.objects.all(),
        'current_query': query or '',
    }
    return render(request, 'library/book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    copies = book.copies.all()
    return render(request, 'library/book_detail.html', {'book': book, 'copies': copies})


@login_required
def reserve_copy(request, copy_id):
    copy = get_object_or_404(Copy, id=copy_id, status='available')
    today = timezone.now().date()
    valid_until = today + timedelta(days=14)

    # utworzenie rezerwacji przez relację odwrotną
    copy.reservations.create(
        user=request.user,
        reserved_at=today,
        valid_until=valid_until,
    )

    copy.status = 'reserved'
    copy.save()

    return redirect('library:book_detail', pk=copy.book.pk)


@login_required
def my_reservations(request):
    reservations = request.user.reservations.select_related('copy__book').all()
    return render(request, 'library/my_reservations.html', {'reservations': reservations})
