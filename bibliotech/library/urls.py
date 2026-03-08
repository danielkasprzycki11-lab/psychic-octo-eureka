from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('copy/<int:copy_id>/reserve/', views.reserve_copy, name='reserve_copy'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
]
