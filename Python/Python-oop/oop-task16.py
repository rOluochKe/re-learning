"""
1. The code begins with the definition of the `Item` class. It has two main methods:
   - The `__init__` method initializes an `Item` object with a `title` and an `author`.
   - The `__str__` method returns a string representation of the `Item` object, displaying the title and author.

2. The `Book` class is defined, which inherits from the `Item` class. It introduces additional functionality:
   - The `__init__` method initializes a `Book` object with a `title`, `author`, and the number of `pages`.
   - The `__len__` method returns the number of pages in the `Book` object when the `len()` function is applied to it.

3. The `DVD` class is defined, also inheriting from the `Item` class. It includes its own unique features:
   - The `__init__` method initializes a `DVD` object with a `title`, `director`, and `duration` in minutes.
   - The `__len__` method returns the duration of the `DVD` object when the `len()` function is applied to it.

4. The `LibraryItem` class is defined, which inherits from both `Book` and `DVD` classes. It combines their attributes:
   - The `__init__` method initializes a `LibraryItem` object with a `title`, `author`, `pages`, `director`, `duration`, and `copies`.
   - It calls the `__init__` methods of both `Book` and `DVD` classes to initialize their respective attributes.
   - The `__str__` method returns a string representation of the `LibraryItem` object, including information about the book's pages and the DVD's duration.
   - The `__add__` method allows adding two `LibraryItem` instances together if they have the same title. It combines their copy counts and returns a new `LibraryItem` object with the updated copy count.

5. In the usage example:
   - An instance of the `Book` class named `book` is created with the title "Python Crash Course", the author "Eric Matthes", and 544 pages.
   - An instance of the `DVD` class named `dvd` is created with the title "Inception", the director "Christopher Nolan", and a duration of 148 minutes.
   - An instance of the `LibraryItem` class named `library_item` is created, representing a combination of the book and DVD. It has the title "Python Crash Course", the author "Eric Matthes", 544 pages, the director "Christopher Nolan", a duration of 148 minutes, and 5 copies.
   - The code demonstrates the usage of various methods:
     - Printing the string representation of `book`, which outputs "Python Crash Course by Eric Matthes".
     - Printing the string representation of `dvd`, which outputs "Inception by Christopher Nolan".
     - Printing the string representation of `library_item`, which outputs "Python Crash Course by Eric Matthes (Book: 544 pages, DVD: 148 minutes)".
     - Getting the length of `book` using `len(book)`, which returns 544.
     - Getting the length of `dvd` using `len(dvd)`, which returns 148.
     - Adding `library_item` to itself and assigning the result to `combined_item`.
     - Printing the string representation of `combined_item`, which shows the combined copy count.
     - Printing the number of copies in `combined_item`, which outputs 10.
"""


class Item:
    def __init__(self, title, author):
        self.name = title
        self.author = author

    def __str__(self):
        return f"{self.name } is by {self.author}"


class Book(Item):
    def __init__(self, title, author, pages):
        Item.__init__(self, title, author)
        self.pages = pages

    def __len__(self):
        return self.pages


class DVD(Item):
    def __init__(self, title, director, duration):
        Item.__init__(self, title, director)
        self.duration = duration

    def __len__(self):
        return self.duration


class LibraryItem(Book, DVD):
    def __init__(self, title, author, pages, director, duration, copies):
        Book.__init__(self, title, author, pages)
        DVD.__init__(self, title, director, duration)
        self.copies = copies
        self.director = director

    def __str__(self):
        return f"{self.name} by {self.author} (Book: {self.pages} pages, DVD: {self.duration} minutes)"

    def __add__(self, other):
        if isinstance(other, LibraryItem) and self.name == other.name:
            combo = self.copies + other.copies
            return LibraryItem(self.name, self.author, self.pages, self.director, self.duration, combo)
        else:
            raise TypeError("Can not add two different objects together!")


book = Book("Harry Potter", "JK Rowling", 500)

dvd = DVD("Inception", "Christopher Nolan", 130)

library_item = LibraryItem(
    "Python Course", "Josh Wenner", 500, "James Cameron", 160, 10)

print(book)
print(dvd)
print(library_item)


print(len(book))
print(len(dvd))


add_items = library_item + library_item
print(add_items)

print(add_items.copies)
