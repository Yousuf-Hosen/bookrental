from django.contrib import admin
from .models import BookTitle,Book
#import export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field
# Register your models here.

class BookResource(resources.ModelResource):
    title=Field()
    status=Field()
    publisher=Field()
    class Meta:
        model=Book
        fields=('title','publisher','isbn','qr_code','status')
        

    def dehydrate_title(self, obj):
        return obj.title.title if obj.title else "not present"
    
    def dehydrate_publisher(self, obj):
        return obj.publisher.name if obj.publisher else "not present"
    
    def dehydrate_status(self, obj):
        return obj.status
    

        

class BookAdmin(ExportActionMixin,admin.ModelAdmin):
    resource_class=BookResource
    
admin.site.register(BookTitle)
admin.site.register(Book,BookAdmin)
