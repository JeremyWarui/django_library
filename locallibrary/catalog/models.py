from django.db import models
import uuid

from django.urls import reverse

from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

# Create your models here.


class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genre (e.g. Science fiction, French Poetry etc.)"
    )

    def __str__(self):
        """String representation of the model object"""
        return self.name

    def get_absolute_url(self):
        """returns the url to access particular genre instances"""
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message="Genre already exists (case-insensitive match)"
            )
        ]


class Book(models.Model):
    """model representing a book - not specific copy"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of the book"),
    isbn = models.CharField('ISBN',
                            max_length=13,
                            unique=True,
                            help_text=''
                            '13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    # ManyToManyField used because genre can contain many books. Books can
    # cover many genres.
    genre = models.ManyToManyField(
        Genre, help_text="Select a genre for this book"
    )
    language = models.ForeignKey(
        'Language', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        """string for representing the model object"""
        return self.title

    def get_absolute_url(self):
        """returns the URL to access a detail record for this book"""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """create a string for the genre. This is required to display genre in Admin"""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """Model representing a specific copy of a book that can be borrowed from the library"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On load'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """string for representing the model object"""
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Model representing an author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """return the URLs to access a particular author instance"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """string representation of the Model object"""
        return f'{self.last_name}, {self.first_name}'


class Language(models.Model):
    """model representing a Language e.g. English, French e.t.c."""
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Enter the book's natural language (e.g. English)")

    def get_absolute_url(self):
        """returns url to access a particular language"""
        return reverse('language-detail', args=[str(self.id)])

    def __str__(self):
        """return string representation of the model"""
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message="Language already exists (case insensitive match)"
            )
        ]
