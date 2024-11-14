from django.contrib import admin
from .models import Book

# Register the Book model with custom admin settings
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the admin list view
    search_fields = ('title', 'author')  # Fields to search by
    list_filter = ('publication_year',)  # Filter by publication year
