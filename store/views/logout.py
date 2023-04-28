from django.contrib.auth.models import User
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.hashers import make_password
from django.shortcuts import render , redirect , HttpResponseRedirect


def signout(request):
              logout(request)
          #     messages.success(request,"successfully logout")
              return redirect('login')