from django.shortcuts import render, redirect
from products.models import Product

from .models import Cart, CartManager


def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	return render(request, "carts/home.html", {})
	

def cart_update(request):
	product_obj = Product.objects.get(id=1)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	if product_obj in cart_obj.products.all():
		cart_obj,products.remove(product_obj)
	else:
		cart_obj.products.add(product_obj)
	#return redirect(product_obj.get_absolute_url())
	return redirect("cart:home")