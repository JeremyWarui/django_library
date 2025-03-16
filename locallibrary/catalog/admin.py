from django.contrib import admin
from .models import Author, Book, BookInstance

# Register your models here.


class BooksInline(admin.TabularInline):
    """Inline admin class for displaying books related to an author."""
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin class for displaying Author model on admin page."""
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class BookInstanceInline(admin.TabularInline):
    """Inline admin class for displaying book instances related to a book.
    on admin page"""
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin class for managing Book model on admin page."""
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    """Admin class for managing BookInstance model on admin page."""
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('Book Information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


# Register the BookInstanceAdmin class with the admin site
admin.site.register(BookInstance, BookInstanceAdmin)
