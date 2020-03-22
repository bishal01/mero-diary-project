

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import List
from .forms import ListForm


def base(request):
    if request.method=='POST':
        form = ListForm(request.POST)
        if form.is_valid():
         form.save()
         all_items=List.objects.all()
         messages.success(request,('Item has been added to list!'))
         return render(request,'base.html',{'all_items':all_items})

    else:
         all_items=List.objects.all()
         return render(request,'base.html',{'all_items':all_items})

def delete(request,List_id):
    item=List.objects.get(pk=List_id)
    item.delete()
    messages.success(request,('Item has been deleted!'))
    return redirect('base')

def cross_off(request,List_id):
    item=List.objects.get(pk=List_id)
    item.completed = True
    item.save()
    return redirect('base')

def uncross(request,List_id):
    item=List.objects.get(pk=List_id)
    item.completed = False
    item.save()
    return redirect('base')