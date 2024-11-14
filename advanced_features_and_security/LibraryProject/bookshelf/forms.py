from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model you're working with (e.g., Book)
        fields = ['title', 'author']