from django.shortcuts import render, get_object_or_404, redirect 
from django.views.decorators.http import require_POST

from shop.models import Product
from .forms import CartAddProductForm
from .cart import Cart 


@require_POST
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product,
			    quantity=cd['quantity'],
			    update_quantity=cd['update'])
	return redirect('cart:cart_detail')

