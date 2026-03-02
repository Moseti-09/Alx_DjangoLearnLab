from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# ==================== FUNCTION-BASED VIEW ====================
def list_books(request):
    """Function-based view: lists ALL books"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ==================== CLASS-BASED VIEW ====================
class LibraryDetailView(DetailView):
    """Class-based view: shows details of ONE specific library"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'   # so template uses {{ library }} instead of {{ object }}