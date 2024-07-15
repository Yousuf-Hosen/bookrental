from django.shortcuts import render
from customers.models import Customer
from books.models import Book,BookTitle
from django.http import HttpResponseRedirect

def change_theme(request):
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode']= not request.session['is_dark_mode']
 
    else:
        request.session['is_dark_mode']=False
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
""" for cahnge the color mode
1. go to tailwind congfig.js
    darkMode: 'class', add  this after  module.exports = { that.
2.create change_theme views 
3. write urls for change_theme views and name=change and path='switch'
4.go to base.html add this class="{% if request.session.is_dark_mode %} dark {% endif %}" in the <html lang='eng' after this >
5. add a link in base.html that namesswitch mode.
<a href="{% url 'change' %}"> switch Mode </a>. here 'change' is the name of the url

    """

def home_view(request):
    obj=BookTitle.objects.get(id=1)
    books=obj.books
    title=obj.title
    print(books)
    print(title)
    qs=Customer.objects.all()
    context={
        'qs':qs,
        'obj':obj,
    }
    return render(request,'main.html',context)