from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def signup(request):
    print("I am running the signup function.")
    if(request.method == "POST"):
        print('It is POST request')
    else:
        print('It is GET method')

    return render(request,'signup.html')



def handlelogin(request):


    return render(request,'login.html')



def handlelogout(request):
   
   
   return render(request,'/auth/login.html')
