from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('bookings/', views.bookings, name='bookings'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('train_details/', views.train_details, name='train_details'),
    path('train_search/', views.train_search, name='train_search'),
    path('book_ticket/<int:train_id>/', views.book_ticket, name='book_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket, name='ticket'),
]