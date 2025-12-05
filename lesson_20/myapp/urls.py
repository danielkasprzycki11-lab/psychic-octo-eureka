from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name='info'),
    path('rules/', views.rules, name='rules'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('products/', views.products_list, name='products_list'),
    path('notes/', views.notes_list, name='notes_list'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('add-product/', views.add_product, name='add_product'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('notes-paginated/', views.notes_list_paginated, name='notes_list_paginated'),
]
