# Django Admin Customization for Book Model

### Step 1: Register the Book Model
Added the following code to `bookshelf/admin.py`:
```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
