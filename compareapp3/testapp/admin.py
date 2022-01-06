from django.contrib import admin
from . models import Product
from . models import Trends,Youtube

class TrendAdmin(admin.ModelAdmin):
    list_display=['id','link','source','created','updated']

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','company1','product1','created','updated']
    list_filter=('company1','product1','company2','product2','company3','product3','company4','product4','product_name')
    prepopulated_fields={'slug':('product_name',)}
    search_fields=('product_name','company1','product1','company2','product2','company3','product3','company4','product4','detail1','detail2','detail3','detail4','name1','name2','name3','name4')

class Youtubeadmin(admin.ModelAdmin):
    list_display=['id','source','source_cat','created','updated']
    List_filter=('created','updated','source_cat')
    search_fields=('source','source_cat')    
    
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Trends,TrendAdmin)
admin.site.register(Youtube,Youtubeadmin)