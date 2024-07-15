from django.db import models
from publishers.models import Publishers
from authors.models import Author
from django.utils.text import slugify
import uuid
#imports for qrcodes generations
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
#for absolate_urls\
from django.urls import reverse
from rentals.choices import STATUS_CHOICES
from .utils import hash_book_info

# Create your models here.



class BookTitle(models.Model): # just a book title that book should be avaiable or not
   
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(blank=True)
    publisher=models.ForeignKey(Publishers,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    @property
    def books(self):
        return self.book_set.all()
    
    def get_absolute_url(self): # if change the urls name values then only chnage in get absulate url function 
        letter=self.title[:1].lower()
        return reverse("books:detail", kwargs={"letter": letter ,"slug": self.slug})
    
    
   
   
    def __str__(self):
       return  str(self.title)
   
    def save(self,*args,**kwargs):
        if not self.slug:
            #generate slug
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)
        
    
        
""" REverse relations
get a  booktitle and find how many books avai;able or all books

the model stands for the actuak model name ,in this case  it wou;d be book_set
obj.model_set.all()  in this case obj.book_set.all()
"""


        

class Book(models.Model): # Physical book available

    """ 
    current status for books
    id 1,2,3
    isbn:unique 24 character long string
    
    future state
    id:36 character long string
    isbn: hashed string based on book title and publisher name
    many BOOKS can have SAME ISBN
    """
    id=models.CharField(primary_key=True,max_length=36,default=uuid.uuid4,editable=False)
    title=models.ForeignKey(BookTitle,on_delete=models.CASCADE) # related_name used for model books then in views use books
    isbn=models.CharField(max_length=64,blank=True)
    #qr_code qr_codes/name.png
    
    # http://127.0.0.1:8000/media/qr_codes/name.png this url show the qr_codes.
    
   # 50249633b31c4e233565b738c45d6a28f38a62564227e5b11d163ffa64f5b991
   # 50249633b31c4e233565b738c45d6a28f38a62564227e5b11d163ffa64f5b991
   
   
    qr_code=models.ImageField(upload_to='qr_codes',blank=True,null=True)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self): # if change the urls name values then only chnage in get absulate url function 
        letter=self.title.title[:1].lower()
        return reverse("books:detail-book", kwargs={"letter": letter ,"slug": self.title.slug,"book_id": self.isbn})
    
    def delete_object(self):
        letter=self.title.title[:1].lower()
        return reverse('books:delete-book',kwargs={'letter':letter,'slug':self.title.slug,"book_id": self.isbn})
    
    def __str__(self):
        return str(self.title)
    
    @property
    def status(self):
        if len(self.rental_set.all()) > 0: #self.modelname_set.all() fetch all books
            statuses=dict(STATUS_CHOICES)
            return statuses[self.rental_set.first().status]
        return False
    
    @property
    def is_available(self):
        if len(self.rental_set.all()) > 0: #self.modelname_set.all() fetch all books # Rental -> rental 
            status=self.rental_set.first().status
            return True if status== '#1' else False
        return True
        
            
    
    def save(self,*args,**kwargs):
        if not self.isbn:
            # self.isbn=str(uuid.uuid4()).replace('-','')[:24]
            self.isbn=hash_book_info(self.title.title,self.title.publisher.name)
            
            #generate qr code
            qrcode_image=qrcode.make(self.isbn)
            canvas=Image.new('RGB',(qrcode_image.pixel_size,qrcode_image.pixel_size),'white')
            canvas.paste(qrcode_image)
            
            fname=f'qr_code-{self.isbn}.png'
            buffer=BytesIO()
            canvas.save(buffer,'PNG')
            self.qr_code.save(fname,File(buffer),save=False)
            canvas.close()
            
    
        
        super().save(*args,**kwargs)
            
    
    
    

