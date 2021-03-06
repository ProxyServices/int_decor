from django.contrib import admin
from .models import Property,PropertyImage,Post
# Register your models here.
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]
    
admin.site.register(Property, PropertyAdmin)
admin.site.register(Post)