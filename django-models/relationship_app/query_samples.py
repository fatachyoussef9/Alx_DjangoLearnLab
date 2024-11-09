import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProjectme.settings")
django.setup()

# Import the models
from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using the related_name 'books'
    for book in books:
        print(f"{book.title} by {book.author.name}")

# Query 2: All books in a specific library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using the related_name 'libraries'
    for book in books:
        print(f"{book.title} is available in {library.name}")

# Query 3: The librarian for a specific library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"{librarian.name} is the librarian for {library.name}")

# Example usage:
if __name__ == "__main__":
    # Replace with the names of the author and library you want to query
    books_by_author('Author Name')
    books_in_library('Library Name')
    librarian_for_library('Library Name')
