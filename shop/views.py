from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def product_list(request, slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if slug:
		category = get_object_or_404(Category, slug=slug)
		products = Product.objects.filter(category=category)
	context = {
	    'category': category,
	    'products': products,
	    'categories': categories
	}
	return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
	products = Product.objects.filter(available=True)[:4]
	product = get_object_or_404(Product, id=id, slug=slug)
	context = {
	    'product': product,
	    'products': products
	}
	return render(request, 'shop/product/detail.html', context)

def home(request):
	return render(request, 'shop/product/list.html')

