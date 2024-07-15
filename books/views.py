from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Book,BookTitle
from django.views.generic import (ListView,
                                  FormView,
                                  DetailView,
                                  DeleteView
)
from .forms import BookTitleForm
from django.urls import reverse,reverse_lazy 
from django.contrib import messages
import string  # for A-Z Letter showing 
# reverse for the fuction or method
# reverse_lazy is going to be classes

# Create your views here.


#function views
# def book_title_list_view(request):
#     qs=BookTitle.objects.all()
#     return render(request,'books/main.html',{'qs': qs})

#class views
class Book_Title_List_View(FormView,ListView):
    # model=BookTitle #Book_Title_List_View is missing a QuerySet. Define Book_Title_List_View.model, Book_Title_List_View.queryset, or override Book_Title_List_View.get_queryset()
    # queryset=BookTitle.objects.all()   # [:x] how many object you would return 
    template_name='books/main.html'
    context_object_name='qs'
    # ordering=('-created',) for ording purpose
    form_class=BookTitleForm
    # success_url=reverse_lazy('books:main') # that not save the forms  for this create form_valid function
    #success_url=reverse_lazy('books:main') instead this we can override get_success_url method 
    
    i_instance=None
    
    def get_success_url(self) :
        return self.request.path
    # we would like to same path so we just return self.request.path
    
    #but the bigghest power is by overriding the get_queryset method
    def get_queryset(self) :
        parameter=self.kwargs.get('letter') if self.kwargs.get('letter')  else 'a' 
        return BookTitle.objects.filter(title__startswith=parameter)    # filter the all booktitle name that startwith 's'
    
    #this is not a convenient approach because you have to redefine everything from the begining.
    # def get_context_data(self):
    #     context = {
    #         'hi':' hello world',
    #         'form':self.get_form_class(),
    #         'qs':self.get_queryset()
    #     }
    #     return context
    
    
    # another approach 

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)  # get all predefine context 
        letters=list(string.ascii_uppercase)
        context['letters'] = letters
        context['selected_letter']=self.kwargs.get('letter') if self.kwargs.get('letter')  else 'a' #check the letter exists or set 'a' as default
        return context
    

    # reverse for the fuction or method
    # reverse_lazy is going to be classes
    def form_valid(self,form):
        self.i_instance = form.save()
        messages.add_message(self.request,messages.INFO, f"Book Title: {self.i_instance.title}  has been created ") 
        # takes 3 parameter1.self.request,what type message,what is the message
        
        return super().form_valid(form)
    
    def form_invalid(self,form) :
        
        self.object_list=self.get_queryset()
        messages.add_message(self.request,messages.ERROR,form.errors)
        
        return super().form_invalid(form)
    

    """ 
    if template_name is not used then only step 5 applicable.
    if context_object_name i not used then step 6 only applicable
    for class based views steps steps:
    1.define class View_name
    2.model=model_name of the particular view
    3.in urls.py import class based views ex. Book_Title_List_View
    4. in path('',class based view_name.as_views,) exam. path('',Book_Title_List_View.as_view(),name='main')
    5.create a html file modelname_list.html example. booktitle_list.html
    6. for query_set in booktitle_list.html . called object_list. example.. {% for el in object_list %}
    
    
    """
    # defalut: model_list.htmlS->booktitle_list.html
    #object list
    

# We have 2 option

#OPTION 1 -> BOOK_LIST VIEW + overriding get_queryset() method
#one of the biggest benefits of this approach is that we can add pagination at very easy way
#1.paginate_by=number_of objects
# class  BookListView(ListView):
#     template_name='books/detail.html'
#     paginate_by=2
    
#     def get_queryset(self):
#         title_slug=self.kwargs.get('slug') 
#         return Book.objects.filter(title__slug=title_slug) # title__slug title is foreign key so for go to upper use __
    

# OPTION 2 -> BOOK TITLE DETAIL VIEW + model method
class BookTitleDetailView(DetailView):
    model=BookTitle
    template_name='books/detail.html'
    
    
class BookDetailView(DetailView):
    model=Book
    template_name='books/detail_book.html'
    
    def get_object(self):
        id=self.kwargs.get('book_id')
        obj=get_object_or_404(Book,isbn=id)
        # obj=Book.objects.get('isbn=id') # this is alternative way
        return obj


class BookDeleteView(DeleteView):
    model=Book
    template_name='books/confirm_delete.html'
    
    def get_object(self):
        id=self.kwargs.get('book_id')
        obj=get_object_or_404(Book,isbn=id)
        # obj=Book.objects.get('isbn=id') # this is alternative way
        return obj
    def get_success_url(self):
        letter=self.kwargs.get('letter')
        slug=self.kwargs.get('slug')
        return reverse('books:detail',kwargs={'letter':letter,'slug':slug})

""" for deleting book 
define a class views name BookDeleteView(DeleteView) inherited from DeleteView
set model= Book Model
1.template_name= delete template nam(as your wish)
2.goto urls.py and import BookDeleteView 
3.add path like this path('<str:letter>/<slug>/<str:book_id>/delete/',BookDeleteView.as_view(),name='delete-book'),
4.override the . get_object method and redirected in BookTitleDetailView  ex:return reverse('books:detail',kwargs={'letter':letter,'slug':slug})

"""

# def book_title_detail_view(request,**kwargs):
#     slug=kwargs.get('slug')
#     obj=BookTitle.objects.get(slug=slug)
#     return render(request,'books/detail.html',{'obj' : obj})

