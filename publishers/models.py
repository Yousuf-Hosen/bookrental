from django.db import models
import uuid
from django_countries.fields import CountryField
# Create your models here.
class Publishers(models.Model):
    """
    Book publishers
    Managed by only in the django admin
    
    id cuiqhdbjhbidh84uyyyuih """
    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200)
    country=CountryField(blank_label='(Select Country)')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.name} from {self.country}"
    
    
