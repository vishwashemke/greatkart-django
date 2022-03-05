from django.contrib import admin
from .models import Product, Variation


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('product_name',)}
    list_display = ('product_name', 'price','stock', 'category','modified_date','is_available')

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category','variation_value', 'created_date','is_active')
    list_editable = ('is_active', )
    list_filter = ('product', 'variation_category','variation_value')

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
