from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView




def list_books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html',{'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name ='relationship_app/library_detail.html'
    context_object_name = 'library'

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'