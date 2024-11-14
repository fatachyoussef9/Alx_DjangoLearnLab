from django.contrib import admin
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser



# Register the Book model with custom admin settings
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the admin list view
    search_fields = ('title', 'author')  # Fields to search by
    list_filter = ('publication_year',)  # Filter by publication year


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# admin.site.register(CustomUser, CustomUserAdmin)
["admin.site.register(CustomUser, CustomUserAdmin)"]
