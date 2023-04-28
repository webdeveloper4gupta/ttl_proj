from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from store.models.orders import Order
# class OrderView(View):
#     def get(self , request ):
#         customer = request.session['customers']
#         print(customer)
#         orders = Order.get_orders_by_customer(customer)
#         print(orders)
#         return render(request , 'orders.html'  , {'orders' : orders})

from  django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def OrderView(request):
              
              
              customer = request.session['customers']
              print(customer)
              a=Order.objects.filter(custid=customer)
              print(a)
              return render(request,"orders.html",{'orders':a})