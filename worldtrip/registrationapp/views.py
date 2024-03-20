from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def register(request):

    if request.method=='POST':
        variable1=request.POST['username']
        variable2=request.POST['first_name']
        variable3=request.POST['last_name']
        variable4=request.POST['email']
        variable5=request.POST['password']
        variable6=request.POST['password1']

        user=User.objects.create_user(username=variable1,password=variable5,first_name=variable2,last_name=variable3,email=variable4)
        user.save();
        print("user created")
    return render(request,"register.html")
