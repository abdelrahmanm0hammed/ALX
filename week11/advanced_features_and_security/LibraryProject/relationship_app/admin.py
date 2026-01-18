from django.contrib import admin

from .models import Book, Author, Library

class BookAdmin(admin.ModelAdmin):
    list_display =('title', )
    search_fields = ('title', 'author') 

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(Author, AuthorAdmin)

admin.site.register(Library)