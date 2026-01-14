from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LoginView.as_view(template_name='relationship_app/logout.html')),
    path('register/',views.SignUp.as_view(), name='register')
]