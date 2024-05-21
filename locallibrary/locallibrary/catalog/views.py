from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Book, Author, BookInstance

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'
    template_name = 'BookList.html'
    ordering = ['title']

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

class AuthorView(generic.ListView):
    model = Author
    paginate_by = 10
    context_object_name = 'authors_list'
    template_name = 'author_list.html'
    ordering = ['last_name'] 

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data here if needed
        return context

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)
