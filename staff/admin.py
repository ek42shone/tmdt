from django.contrib import admin

# Register your models here.
from staff.models import StorageStaff, Storage, Fullname, Address, Product, Manufacturer, Item, ItemInCart, Cart, \
    ProductImage, Clothing,Order


class productAdmin(admin.ModelAdmin):
    list_display=['name','price','image_tag','status','type']
    search_fields = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display=['name','price','image_tag','status','type']

admin.site.register(Storage)
admin.site.register(Fullname)
admin.site.register(Address)
admin.site.register(StorageStaff)
admin.site.register(Product, productAdmin)
admin.site.register(Manufacturer)
admin.site.register(Item)
admin.site.register(ItemInCart)
admin.site.register(Cart)
admin.site.register(ProductImage)
admin.site.register(Clothing)
admin.site.register(Order)
