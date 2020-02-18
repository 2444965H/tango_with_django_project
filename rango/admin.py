from django.contrib import admin
from rango.models import UserProfile

# Register your models here.
# Chapter 5.5

from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    #alt
    list_display = ('title','category','url','views')
    

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)