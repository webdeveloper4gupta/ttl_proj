from django.shortcuts import render , redirect , HttpResponseRedirect
# from django.contrib.auth.hashers import  check_password
# from store.models.customer import Customer
# from django.views import View
# from django.contrib.auth import authenticate, login, logout 

# class Login(View):
#     return_url = None

#     def get(self, request):
#         Login.return_url = request.GET.get ('return_url')
#         return render (request, 'login.html')

#     def post(self, request):
#         email = request.POST.get ('email')
#         password = request.POST.get ('password')
#         customer = Customer.get_customer_by_email (email)
#         error_message = None
#         if customer:
#             flag = check_password (password, customer.password)
#             if flag:
#                 request.session['customer'] = customer.id
           
              
            

#                 if Login.return_url:
#                     return HttpResponseRedirect (Login.return_url)
#                 else:
#                     Login.return_url = None
#                     return redirect ('homepage')
#             else:
#                 error_message = 'Invalid !!'
#         else:
#             error_message = 'Invalid !!'

#         print (email, password)
#         return render (request, 'login.html', {'error': error_message})

# def logout(request):
#     request.session.clear()
#     return redirect('login')




# now here i write the code for login
from django.contrib.auth.models import User
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.hashers import make_password



def Login(request):
              if request.method == 'POST':
                    name = request.POST.get('name')
                    password = request.POST.get('password')

                    user = authenticate(request,username=name, password=password)
        
                    if user is not None:
                        firstname = user.first_name
            
                        login(request,user)
                        request.session['customers'] = user.id
                        print(user.id)
                        # a = contacts.objects.all()
                        return render(request, "index.html")
                    else:
                        # messages.error(request, "please try again")
                        return redirect(Login)
              return render(request, "login.html")