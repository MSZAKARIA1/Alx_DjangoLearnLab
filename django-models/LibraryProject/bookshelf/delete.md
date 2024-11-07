
# Delete the Book Instance
```python
from bookshelf.models import Book
book.delete()
Book.objects.all()
# Expected output: <QuerySet []>
