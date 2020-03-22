
from django.shortcuts import render, redirect
from .models import memory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.utils import timezone
from django.http import HttpResponseRedirect




@login_required(login_url='login')
def ok(request):
    return render(request,"ok.html")




@login_required(login_url='login')
def view(request) :
  log_user=request.user
  memories=memory.objects.filter(user=log_user)
  return render(request,"view.html",{'m':memories})



@login_required(login_url='login')
def add(request):
    if request.method=="POST":
     data=request.POST['data']
     new=memory(content=data,user=request.user)
     new.save()
     messages.success(request, f'saved sucessfully')
     return render(request,"add.html")
    else:
     return render(request,"add.html")




@login_required(login_url='login')
def calulator(request):
    return render(request, "calculator.html")



@login_required(login_url='login')
def calender(request):
    return render(request, "calender.html")



def games(request):
    return render(request, "games.html")



# Create your views here.

