from django.shortcuts import render
from testApp.models import Book
from django.views.generic import ListView,DetailView
# Create your views here.


class BookListView(ListView):
    model = Book
    #template_name = 'testApp/books.html'
    #context_object_name = 'list_of_books'
# defalut template: book_List.html
# defalut context object : book_list

class BookDetailView(DetailView):
    model = Book