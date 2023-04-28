from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from store.models.ratings import Ratings
def dels(request,pk1):
          g1=Ratings.objects.get(id=pk1)
          g1.delete()
          # now i udate the rating score here
          d=request.session['prodid']
          print(d)
          # now i start writing the concept of deleting the rating 
          data=Ratings.objects.filter(prodid=d)
          print(data,"here i print the data")
          if len(data)>0:
                              averages=0
                              sums=0
                              count=0
                              for d in data:
                                          sums+=d.rating
                                          count+=1
                              averages=sums/count 
                              
                              print(averages)
                              # now here i have to save the rating in the product database 
                              p1=Products.objects.get(id=d)
                              p1.avgrat=averages 
                              p1.save()
          else:
                    
                    averages=0  
                    p1=Products.objects.get(id=d)
                    p1.avgrat=averages 
                    p1.save()
          
          return render(request,"rating.html")