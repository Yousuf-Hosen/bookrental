from typing import Any
from django import forms
from .models import BookTitle
from django.core.exceptions import ValidationError

class BookTitleForm(forms.ModelForm):
    class Meta:
        model=BookTitle # in meta tell what model we are using
        fields=('publisher','author','title')
        
    def clean(self):
        title=self.cleaned_data.get('title')
        if len(title) < 5:
            self.add_error('title','the title is too short') 
            # raise ValidationError('the title is too short') # general error for form_non_fields_errors
        book_title_exists=BookTitle.objects.filter(title__iexact=title).exists()
        if book_title_exists:
            self.add_error('title','this is book title already exists')
        return self.cleaned_data

#here basically 2 option
# forms.ModelForm  -> whenever we want to do something with the model in this form ..we are going to add a book title
#forms.Form  when we don't want to refer to a model
# in this project we are gong to create two such forms 1.for the search 2.select export model




""" there 2 ways to created forms
1.ordinary Html forms
2. django forms
django forms has to nore powerful features so we use it
steps:
1.create a forms.py file in the apps
2.in forms.py import necessary libraries from django import forms
from .models import BookTitle for use BookTitle model import it here
3.create class Forms_name(inherited from forms.Modelform) #ex: class BookTitleForm(forms.ModelForm):
4.Decleare class Meta and tell which model you want to use and how many fields you want 
ex: model=BookTitle 
    fields=('title','publisher','author')
5. in apps_name:models.py 's class based views add parameter form_class=forms.py's class name
ex. form_class=BookTitleForm before this import it
6. in html_file in this project main.html create a form with method="POST">
import csrf token
{{form}}
    

"""