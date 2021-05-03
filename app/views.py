from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
def index(request):
    return render(request,'index.html')
def help(request):
    return render(request,'help.html')

def login(request): 
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect("login")
    else: 
        return render(request,'login.html')
def reg(request): 
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
       # password2=request.POST['password2']
        user=User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        return redirect("/")
    else:
        return render(request,'reg.html') 
def career(request):    
    return render(request,'career.html')  
def careertest(request):    
    return render(request,'careertest.html')  
def careertool(request):    
    return render(request,'careertool.html')        
def logout(request):
    auth.logout(request)
    return redirect("/") 
def contact(request):
    return render(request,'contact.html') 
def earnings(request):
    return render(request,'earnings.html')     


# Create your views here.
