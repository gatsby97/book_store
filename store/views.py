from django.shortcuts import render,get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg
# Create your views here.
def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request,"/home/russet_potato/switch_study/book_store/store/templates/index.html",{
        "books":books,
        "total_no_books":num_books,
        "avg_rating":avg_rating
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug= slug)
    return render(request,"/home/russet_potato/switch_study/book_store/store/templates/book_detail.html",{
        'title':book.title,
        'author':book.author,
        'rating':book.rating,
        'is_bestseller':book.is_bestselling
        } )
    