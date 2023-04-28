from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login 
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views import viewss
from .views.logout import  signout
from .views.update import upd
from .views.delete import dels

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    # path('signup', Signup.as_view(), name='signup'),
    # path('login', Login.as_view(), name='login'),
    path('login',Login,name='login'),
    path('signup',Signup,name='signup'),
    path('logout', signout , name='logout'),
    path('cart', Cart , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', OrderView, name='orders'),
    path('rating/<int:pk>',viewss.rating,name='rating'),
    path('mahajan/<int:pk1>',dels,name="mahajan"),
    path('update/<int:pk2>',upd,name='update')
]
