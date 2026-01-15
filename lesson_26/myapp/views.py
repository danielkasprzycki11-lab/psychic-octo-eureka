from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category


# ZADANIE 2 - Widok kategorii
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'myapp/category_detail.html', context)


# ZADANIE 3 - Ostatnie 5 postów
def home(request):
    latest_posts = Post.objects.order_by('-id')[:5]
    
    context = {
        'posts': latest_posts
    }
    return render(request, 'myapp/home.html', context)


# ZADANIE 6 - Wyszukiwarka
def search_posts(request):
    query = request.GET.get('q', '')
    posts = []
    
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    
    context = {
        'query': query,
        'posts': posts,
        'results_count': posts.count()
    }
    return render(request, 'myapp/search_results.html', context)
