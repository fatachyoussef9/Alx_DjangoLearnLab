from django.shortcuts import render, redirect

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .models import Book  # Assuming you have a Book model

def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})
["book_list"]
@permission_required('bookshelf.can_create', raise_exception=True)
def create_object(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('object_list')  # Redirect to list of objects
    else:
        form = UserProfile()
    return render(request, 'bookshelf/form_example.html', {'form': form})



@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_yourmodel(request, pk):
    instance = get_object_or_404(UserProfile, pk=pk)
    # Your editing logic here
    return render(request, 'yourmodel/edit.html', {'instance': instance})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_object(request, pk):
    obj = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('object_list')  # Redirect to list of objects
    return render(request, 'bookshelf/confirm_delete.html', {'object': obj})


@permission_required('bookshelf.can_view', raise_exception=True)
def view_object(request, pk):
    obj = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'bookshelf/detail_view.html', {'object': obj})