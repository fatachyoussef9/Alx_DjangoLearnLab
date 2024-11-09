import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProjectme.settings")
django.setup()

# Import the models
from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Using the related_name 'books'
        if books.exists():
            print(f"Books by {author.name}:")
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found for author: {author_name}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

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
    # Example: Replace with the names of the author and library you want to query
    author_name = 'Author Name'  # Replace with the author's name
    library_name = 'Library Name'  # Replace with the library's name

    # Query for all books by the author
    print("Checking books by author:")
    books_by_author(author_name)

    # Query for all books in the library
    print("\nChecking books in library:")
    books_in_library(library_name)

    # Query for the librarian for a library
    print("\nChecking librarian for library:")
    librarian_for_library(library_name)
