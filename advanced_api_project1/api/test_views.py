#  a) Testing CRUD Operations:

from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test author
        self.author = Author.objects.create(name="J.K. Rowling")
        # Create a test book
        self.book = Book.objects.create(title="Harry Potter 1", publication_year=1997, author=self.author)

    def test_create_book(self):
        # Test creating a new book
        url = '/api/books_all/'
        data = {'title': 'Harry Potter 2', 'publication_year': 1998, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book_list(self):
        # Test retrieving the list of books
        url = '/api/books_all/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_book_detail(self):
        # Test retrieving a single book by ID
        url = f'/api/books_all/{self.book.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        # Test updating an existing book
        url = f'/api/books_all/{self.book.id}/'
        data = {'title': 'Harry Potter 1 - Updated', 'publication_year': 1997, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Harry Potter 1 - Updated')

    def test_delete_book(self):
        # Test deleting a book
        url = f'/api/books_all/{self.book.id}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)


#  b) Testing Filtering, Searching, and Ordering:

class BookFilteringTests(APITestCase):

    def setUp(self):
        self.author1 = Author.objects.create(name="J.K. Rowling")
        self.author2 = Author.objects.create(name="George Orwell")
        self.book1 = Book.objects.create(title="Harry Potter 1", publication_year=1997, author=self.author1)
        self.book2 = Book.objects.create(title="1984", publication_year=1949, author=self.author2)

    def test_filter_books_by_title(self):
        # Test filtering books by title
        url = '/api/books_all/?title=Harry Potter'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_author(self):
        # Test filtering books by author
        url = f'/api/books_all/?author={self.author1.id}'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        # Test ordering books by publication year
        url = '/api/books_all/?ordering=publication_year'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], '1984')  # Oldest first

    def test_search_books_by_title(self):
        # Test searching books by title
        url = '/api/books_all/?search=Harry'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


#  c) Testing Permissions:

class BookPermissionsTests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter 1", publication_year=1997, author=self.author)

    def test_permission_required_to_create_book(self):
        # Test that an unauthenticated user cannot create a book
        url = '/api/books_all/'
        data = {'title': 'Harry Potter 2', 'publication_year': 1998, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permission_required_to_update_book(self):
        # Test that an unauthenticated user cannot update a book
        url = f'/api/books_all/{self.book.id}/'
        data = {'title': 'Harry Potter 1 - Updated', 'publication_year': 1997, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):
        # Test that an authenticated user can create a book
        self.client.force_authenticate(user=self.user)
        url = '/api/books_all/'
        data = {'title': 'Harry Potter 2', 'publication_year': 1998, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
