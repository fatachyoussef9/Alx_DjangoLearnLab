from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
# Expected Output:
# (1, {'bookshelf.Book': 1})
Book.objects.all()
# Confirm that the book was deleted
