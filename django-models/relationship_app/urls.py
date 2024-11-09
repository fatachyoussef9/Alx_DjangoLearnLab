from .views import list_books

from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  
    # URL for the function-based view (list of books)
    path('books/', views.list_books, name='list_books'),
    
    # URL for the class-based view (library details)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # URL for logout (using Django's built-in LogoutView)
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # URL for registration (using the custom register view)
    path('register/', views.register, name='register'),
]