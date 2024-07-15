from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .forms import SearchBookForm
from books.models import Book
from django.views.generic import ListView
from .models import Rental

# Create your views here.

def search_book_view(request):
    form = SearchBookForm(request.POST or None)
    search_query=request.POST.get('search', None)                 # search fields that defies in forms.py 
    book_ex=Book.objects.filter(isbn=search_query).exists()
    if search_query is not None and book_ex:
        # redirected to the detail page { rentals list of the books }
        return redirect('rentals:detail',search_query)
    context={
        'form':form,
    }
    return render(request,'rentals/main.html',context)


class BookRentalHistoryView(ListView):
    model=Rental # Rental.objects.all()
    template_name= 'rentals/detail.html'
    def get_queryset(self):
        book_id=self.kwargs.get('book_id')
        return Rental.objects.filter(book__isbn=book_id) #__ refers the foreign key relation
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs=self.get_queryset()
        obj=None
        if qs.exists():
            obj=qs.first()
        context['object']=obj
        return context
    
        """ 
    current status for books
    id 1,2,3
    isbn:unique 24 character long string
    
    future state
    id:36 character long string
    isbn: hashed string based on book title and publisher name
    many BOOKS can have SAME ISBN
    
    """
    
       
    