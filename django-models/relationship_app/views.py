from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import UserProfile

from django.views.generic.detail import DetailView

from django.shortcuts import render

from .models import Library
# Create your views here.
from .models import Book
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import registration
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template for the library details page
    context_object_name = 'library'


    
def user_is_admin(user):
    return user.profile.role == 'Admin'


def user_is_librarian(user):
    return user.profile.role == 'Librarian'

def user_is_member(user):
    return user.profile.role == 'Member'

# Admin View (Only for Admin users)
@login_required
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View (Only for Librarian users)
@login_required
@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View (Only for Member users)
@login_required
@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')