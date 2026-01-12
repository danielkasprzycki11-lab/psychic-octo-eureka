def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Product, Note, Category
from .forms import ProductForm

# ZADANIE 1
def info(request):
    return HttpResponse("Informacje o stronie")

def rules(request):
    return HttpResponse("Regulamin serwisu")

# ZADANIE 2
def user_profile(request, username):
    return render(request, 'user_profile.html', {'username': username})

# ZADANIE 4
def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

# ZADANIE 6
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes_list.html', {'notes': notes})

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'note_detail.html', {'note': note})

# ZADANIE 7
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# ZADANIE 9
def category_products(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    category = Category.objects.get(id=category_id)
    return render(request, 'category_products.html', {
        'products': products,
        'category': category
    })

# ZADANIE 10
def notes_list_paginated(request):
    all_notes = Note.objects.all()
    paginator = Paginator(all_notes, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'notes_list_paginated.html', {'page_obj': page_obj})

from django.shortcuts import render
from .models import Entry


def entry_list_view(request):
    """Widok wyświetlający wszystkie wpisy blogowe."""
    all_entries = (
        Entry.objects
        .select_related("blog")
        .prefetch_related("authors")
        .order_by("-pub_date")
    )

    context = {
        "entries": all_entries,
    }
    return render(request, "blog/entry_list.html", context)
