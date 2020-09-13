from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def loginpage(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request,username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect('blog.page')
         else:
            print("invalid username and password!")
        
    return render(request,'authentication/login.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
              print('username is already exits!')
            elif User.objects.filter(email = email).exists():
               print("Email is already exits!")
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
        else:    
          print("Sorry password does't match")

    return render(request,'authentication/registration.html')

def forgotpassword(request):
    return render(request,'authentication/forgotpassword.html')
    
def signout(request):
    logout(request)
    return redirect('login.page')
