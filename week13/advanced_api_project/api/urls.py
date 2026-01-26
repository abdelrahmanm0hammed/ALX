from django.urls import path

from .views import (BookUpdateView, BookCreateView, BookDeleteView, BookDetailView, BookListView)

urlpatterns = [

   path('books/', BookListView.as_view(), name='book-list'),
   path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
   path('books/create/', BookCreateView.as_view(), name='book-create'),
   path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
   path('book/detail/<int:pk>/', BookDetailView.as_view(), name='book-detail')                 


]