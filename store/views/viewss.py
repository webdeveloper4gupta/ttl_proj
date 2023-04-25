from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.ratings import Ratings
def rating(request,pk):
                  
        
                  print(pk)
                #   here i use the product id for fetching the details of the product
                  if request.method=='POST':
                                    text=request.POST.get('textarea')
                                    rating=request.POST.get('rat')
                                    Ratings(name=text,rating=rating,prodid=pk).save()
                  data=Ratings.objects.filter(prodid=pk)
                  return render(request,"rating.html",{'data':data})