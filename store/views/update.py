# here i write the view for the update 
from django.shortcuts import render , redirect , HttpResponseRedirect 
from store.models.ratings import Ratings
from  django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def upd(request,pk2):
          print(pk2)
          if request.method=='POST':
                     text=request.POST.get('textarea')
                     rating=request.POST.get('rat')
                     r1=Ratings.objects.get(id=pk2)
                     r1.name=text
                     r1.rating=rating
                     r1.save()
                     return render(request,"index.html")
                    # Ratings(name=text,rating=rating,prodid=pk,custname=a1.username,custid=a1.id).save()
                    
          return render(request,"update.html")