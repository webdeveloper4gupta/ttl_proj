from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
# from store.models.customer import Customer
# from django.views import View


# class Signup (View):
#     def get(self, request):
#         return render (request, 'signup.html')

#     def post(self, request):
#         postData = request.POST
#         first_name = postData.get ('firstname')
#         last_name = postData.get ('lastname')
#         phone = postData.get ('phone')
#         email = postData.get ('email')
#         password = postData.get ('password')
#         # validation
#         value = {
#             'first_name': first_name,
#             'last_name': last_name,
#             'phone': phone,
#             'email': email
#         }
#         error_message = None

#         customer = Customer (first_name=first_name,
#                              last_name=last_name,
#                              phone=phone,
#                              email=email,
#                              password=password)
#         error_message = self.validateCustomer (customer)

#         if not error_message:
#             print (first_name, last_name, phone, email, password)
#             customer.password = make_password (customer.password)
#             customer.register ()
#             return redirect ('homepage')
#         else:
#             data = {
#                 'error': error_message,
#                 'values': value
#             }
#             return render (request, 'signup.html', data)

#     def validateCustomer(self, customer):
#         error_message = None
#         if (not customer.first_name):
#             error_message = "Please Enter your First Name !!"
#         elif len (customer.first_name) < 3:
#             error_message = 'First Name must be 3 char long or more'
#         elif not customer.last_name:
#             error_message = 'Please Enter your Last Name'
#         elif len (customer.last_name) < 3:
#             error_message = 'Last Name must be 3 char long or more'
#         elif not customer.phone:
#             error_message = 'Enter your Phone Number'
#         elif len (customer.phone) < 10:
#             error_message = 'Phone Number must be 10 char Long'
#         elif len (customer.password) < 5:
#             error_message = 'Password must be 5 char long'
#         elif len (customer.email) < 5:
#             error_message = 'Email must be 5 char long'
#         elif customer.isExists ():
#             error_message = 'Email Address Already Registered..'
#         # saving

#         return error_message


# now here i implement the concept of adding the user in User database 
from django.contrib.auth.models import User
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.hashers import make_password




def Signup(request):
              if request.method=="POST":
                username=request.POST.get('name')
                firstname=request.POST.get('firstname')
                lastname=request.POST.get('lastname')
                email=request.POST.get('email')
                password1=request.POST.get('password')
                print("hello 1")
                if User.objects.filter(username=username):
                    # messages.error(request,"usernam already exist")
                    return redirect(Signup) 
                if User.objects.filter(email=email):
                    # messages.error(request,"email already exist")
                    return redirect(Signup)
     
                user=User.objects.create_user(username,email)
                user.set_password(password1)
                user.first_name=firstname
        # user.is_staff=True
       
                user.last_name=lastname
                user.is_active=True
                user.save()
                # messages.success(request,"succesfully created user")
        
       

                return redirect('homepage')
    
              return render(request,"signup.html")
    
