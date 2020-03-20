from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.get_fields()]
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
