from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

# class Cart(View):
#     def get(self , request):
#         ids = list(request.session.get('cart').keys())
#         products = Products.get_products_by_id(ids)
#         print(products)
#         return render(request , 'cart.html' , {'products' : products} )

from  django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def Cart(request):
    ids=request.session['prodid']
    print(ids)
    a=Products.objects.get(id=ids)
    return render(request,"cart.html",{'products':a})