from django.core.management.base import BaseCommand

from authors.models import Author
from publishers.models import Publishers
from books.models import Book,BookTitle
from customers.models import Customer
from django_countries.fields import Country
import random
""" 
1.create folder management
2.inside aniother folder commands
3.generate_dummy_data.py

"""
class Command(BaseCommand):
    
    help= "Generate Dummy Data for testing purposes"
    def handle(self,*args,**kwargs):
        
        #Generating authors
        author_list=['John Smith','Adam Jones','Jane Johnson','Megan Tylor']
        for name in author_list:
            Author.objects.create(name=name)
            
        # Generating Publishers
        publishers_list=[
            {'name':'X Books','country':Country(code='us')},
            {'name':'Bookz' ,'country':Country(code='de')},
            {'name':'Edu Mind','country':Country(code='gb')},
            {'name':'Next','country':Country(code='pl')},
        ]
        for item in publishers_list:
            Publishers.objects.create(**item)
        
        
        #Generating book titles
        
        book_titles_list=['Harry Zotter','Lord of the Wings','Django Made Easy','Switcher','Automation with Python ']
        publishers=[x.name for x in Publishers.objects.all()]
        items=zip(book_titles_list,publishers)
        for item in items:
            author=Author.objects.order_by('?')[0]
            publisher=Publishers.objects.get(name=item[1])
            BookTitle.objects.create(title=item[0],publisher=publisher,author=author,)
            
            
        
        
        #Generating books
        
        book_titles=BookTitle.objects.all()
        for title in book_titles:
            quantity=random.randint(1,5)
            for i in range(quantity):
                Book.objects.create(title=title)

        #Generating customers
        
        
        customers_list=[
            {'first_name':'John','last_name': 'Doe'},
            {'first_name':'Adam','last_name': 'Harris'},
            {'first_name':'Lisa','last_name': 'Martinz'},
            {'first_name':'Martin','last_name': 'Hooke'}
        ]
        
        for item in customers_list:
            Customer.objects.create(**item)
        