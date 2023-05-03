from django.shortcuts import render , redirect , HttpResponseRedirect

def aboutus(request):
          return render(request,"aboutus.html")