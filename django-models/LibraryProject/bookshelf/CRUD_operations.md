

<!-- # Create a Book Instance -->
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected output: <Book: 1984 by George Orwell published on 1949>


# Retrieve a Book Instance
```python
book = Book.objects.get(title="1984")
book
# Expected output: <Book: 1984 by George Orwell published on 1949>


# Update the Title of the Book
```python
book.title = "Nineteen Eighty-Four"
book.save()
book
#Expected output: <Book: Nineteen Eighty-Four by George Orwell published on 1949>


# Delete the Book Instance
```python
book.delete()
Book.objects.all()
# Expected output: <QuerySet []>