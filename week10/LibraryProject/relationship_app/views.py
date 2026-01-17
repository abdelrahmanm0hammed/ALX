from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import  redirect, get_object_or_404



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


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'ADMIN'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'LIBRARIAN'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'MEMBER'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):

    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year= publication_year)
        return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, pk):
    book = get_object_or_404(Book , pk=pk)
    if request.method == "POST":
        book.title =request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('list_books')
    return render (request, 'relationship_app/change_book.html',{'book':book})

@login_required
@permission_required('relationship_app.can_delete.book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html',{'book':book})