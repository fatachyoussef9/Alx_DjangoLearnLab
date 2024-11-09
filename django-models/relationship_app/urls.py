from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  
    # URL for the function-based view (list of books)
    path('books/', views.list_books, name='list_books'),
    
    # URL for the class-based view (library details)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]