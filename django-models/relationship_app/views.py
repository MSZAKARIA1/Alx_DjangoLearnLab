# adding a function-based view that retrieves all books and displays their titles and authors:
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
    
#adding a class-based view to display details for a specific library, listing all books available in that library.
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Access all books related to the library
        return context

