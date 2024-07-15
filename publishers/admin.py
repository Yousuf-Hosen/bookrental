from django.contrib import admin
from .models import Publishers
#import-export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# Register your models here.

class PublisherResource(resources.ModelResource):
    date=Field() # instance of field now write a function below name: def dehydrate_fields_name 
    class Meta:
        model=Publishers
        fields=('id','name','coutry','created','date')
        export_order=fields
        
    def dehydrate_date(self,obj):
        return obj.created.strftime("%d/%m/%y")
        
class PublisherAdmin(ExportActionMixin,admin.ModelAdmin): # without ExportActionMixin  download options doesnot show in admin selected fields
    resources_class=PublisherResource

admin.site.register(Publishers,PublisherAdmin)
