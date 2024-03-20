from django.shortcuts import render
from django.http import HttpResponse
from . models import collegeproject
# Create your views here.
def demo(request):
    #name="noufal"
    #return render(request,"home.html",{'obj':name})
    obj=collegeproject.objects.all()
    return render(request,"index.html",{'result':obj})

#def result(request):

    #x=int(request.GET['number1'])
    #y=int(request.GET['number2'])
    #total=x+y
    #return render(request,"result.html",{'result':total})