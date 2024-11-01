from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display the specified fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filter options for publication year
    list_filter = ('publication_year',)

    # Enable search functionality for title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin configuration
admin.site.register(Book, BookAdmin)

