from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.ratings import Ratings
# here i make the authentication system 
from django.contrib.auth.models import User
from  django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def rating(request,pk):
                  print(pk)
                #   here i use the product id for fetching the details of the product
                  if request.method=='POST':
                                    text=request.POST.get('textarea')
                                    rating=request.POST.get('rat')
                                    Ratings(name=text,rating=rating,prodid=pk).save()
                  data=Ratings.objects.filter(prodid=pk)
                  # here i write the concept of the average rating 
                  # print(len(data),'the length of the data is')
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
                              p1=Products.objects.get(id=pk)
                              p1.avgrat=averages 
                              p1.save()
                                          
                              
                  return render(request,"rating.html",{'data':data})