from catalog.models import Author, Book, Genre, Language, BookInstance
import django
from datetime import date

# Ensure Django settings are configured
django.setup()

# Add genres
genre1 = Genre.objects.create(name="Science Fiction")
genre2 = Genre.objects.create(name="Fantasy")
genre3 = Genre.objects.create(name="Mystery")
genre4 = Genre.objects.create(name="Non-fiction")
genre5 = Genre.objects.create(name="French Poetry")

# Add authors
author1 = Author.objects.create(first_name="Isaac", last_name="Asimov", date_of_birth=date(
    1920, 1, 2), date_of_death=date(1992, 4, 6))
author2 = Author.objects.create(
    first_name="J.K.", last_name="Rowling", date_of_birth=date(1965, 7, 31))
author3 = Author.objects.create(first_name="Agatha", last_name="Christie", date_of_birth=date(
    1890, 9, 15), date_of_death=date(1976, 1, 12))
author4 = Author.objects.create(
    first_name="Margaret", last_name="Atwood", date_of_birth=date(1939, 11, 18))
author5 = Author.objects.create(
    first_name="Homer", last_name="Homer", date_of_birth=None, date_of_death=None)

# Add languages
language1 = Language.objects.create(name="English")
language2 = Language.objects.create(name="French")
language3 = Language.objects.create(name="Spanish")
language4 = Language.objects.create(name="German")
language5 = Language.objects.create(name="Italian")

# Add books
book1 = Book.objects.create(
    title="Foundation", author=author1, isbn="9780553382570", language=language1,
    summary="A complex saga of humans scattered on planets throughout the galaxy all living under the rule of the Galactic Empire.")
book1.genre.add(genre1, genre2)

book2 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone",
                            author=author2, isbn="9780747532699", language=language1,
                            summary="A young boy discovers he is a wizard on his 11th birthday when Hagrid escorts him to magic-teaching Hogwarts School.")
book2.genre.add(genre2)

book3 = Book.objects.create(title="Murder on the Orient Express",
                            author=author3, isbn="9780062693662", language=language1,
                            summary="Detective Hercule Poirot solves a murder mystery on the famous train, the Orient Express.")
book3.genre.add(genre3)

book4 = Book.objects.create(title="The Handmaid's Tale",
                            author=author4, isbn="9780385490818", language=language1,
                            summary="A dystopian novel set in a totalitarian society ruled by a theocracy that treats women as property of the state.")
book4.genre.add(genre1)

book5 = Book.objects.create(
    title="The Iliad", author=author5, isbn="9780140275360", language=language2,
    summary="An ancient Greek epic poem attributed to Homer, detailing the events of the Trojan War.")
book5.genre.add(genre4)

# Add book instances (uncomment these lines if you want to add Book Instances)
book_instance1 = BookInstance.objects.create(
    book=book1, imprint="1st Edition", due_back=date(2025, 4, 20), status="a")
book_instance2 = BookInstance.objects.create(
    book=book2, imprint="1st Edition", due_back=date(2025, 5, 15), status="o")
book_instance3 = BookInstance.objects.create(
    book=book3, imprint="1st Edition", due_back=date(2025, 4, 10), status="r")
book_instance4 = BookInstance.objects.create(
    book=book4, imprint="1st Edition", due_back=None, status="m")

# Print confirmation
print("Sample data added successfully!")
