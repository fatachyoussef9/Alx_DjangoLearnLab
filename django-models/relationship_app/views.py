from django.views.generic.detail import DetailView

from django.shortcuts import render

from .models import Library
# Create your views here.
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template for the library details page
    context_object_name = 'library'