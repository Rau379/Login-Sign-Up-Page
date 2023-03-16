from django.shortcuts import render,HttpResponse, redirect
#importing the user model to run a query
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
#importing to ensure that if user is authenticate only then he can enter the home page 
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html' )
 
def SignuPage(request):
    if request.method=='POST':
        uname= request.POST.get('username')
        email=request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2=request.POST.get('password2')
        #constraint for not having same password
        if pass1!=pass2:
            return HttpResponse("Your password do not match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            #return HttpResponse("User has been created Successfully!!!")
            return redirect('login') 
    return render(request, 'signup.html')

def LoginPage(request):
    #handling data of logi page
    if request.method=='POST':
        username= request.POST.get('username')
        pass1=request.POST.get('pass')
        #checking the correct password and username for login
        user=authenticate(request, username=username, password=pass1)
        #if not present then redirect to login page
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")
        #print(username, pass1)
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')