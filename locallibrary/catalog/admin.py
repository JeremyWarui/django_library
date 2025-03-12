from django.contrib import admin

from .models import Author, Book, BookInstance, Language, Genre
# Register your models here.

# admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(Language)
# admin.site.register(BookInstance)
# admin.site.register(Author)

class BooksInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
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


# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
