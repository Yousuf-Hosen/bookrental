from django.contrib import admin
from .models import Customer
#import-export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# Register your models here.
class CustomerResource(resources.ModelResource):
    aditional_info=Field()
    books=Field()
    class Meta:
        model=Customer
        fields=("id","first_name","last_name","username","aditional_info","rating","books","book_count")
        export_order=fields
    def dehydrate_aditional_info(self,obj):
        if len(obj.aditional_info)==0:
            return "-"
        elif len(obj.aditional_info)<5:
            return obj.aditional_info
        else:
            text_list=obj.aditional_info.split(" ")[:5]
            return " ".join(text_list)+"..."
    
    def dehydrate_books(self,obj):
        books=[x.isbn for x in obj.books.all()]
        return " | ".join(books)
class CustomerAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class=CustomerResource
    
admin.site.register(Customer,CustomerAdmin)
