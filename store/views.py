from django.shortcuts import render,redirect
from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def reg(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('booklist')
    else:
        form = UserCreationForm()
    return render(request ,'register.html', {'form':form})

def log(request):
    form = UserCreationForm()
    return render(request ,'login.html', {'form':form})




# book list functions

def book_list(request):
    return render(request,'base/book_list.html')

# list

def c(request):
    post = Computer.objects.all()
    return render(request,'departments/Computer.html', {'post':post})

def el(request):
    post = Electrical.objects.all()
    return render(request,'departments/Electrical.html', {'post':post})

def e(request):
    post = Electronic.objects.all()
    return render(request,'departments/Electronics.html', {'post':post})

def ci(request):
    post = Civil.objects.all()
    return render(request,'departments/Civil.html', {'post':post})

def m(request):
    post = Mechanical.objects.all()
    return render(request,'departments/Mechanical.html', {'post':post})

# functions

def comp(request, pk):
    post = get_object_or_404(Computer, pk=pk)
    return render(request,'c_list.html',{'post':post})

def elec(request, pk):
    post = get_object_or_404(Electrical, pk=pk)
    return render(request,'el_list.html',{'post':post})

def electro(request, pk):
    post = get_object_or_404(Electronic, pk=pk)
    return render(request,'e_list.html',{'post':post})

def mech(request, pk):
    post = get_object_or_404(Mechanical, pk=pk)
    return render(request,'m_list.html',{'post':post})

def civ(request, pk):
    post = get_object_or_404(Civil, pk=pk)
    return render(request,'cv_list.html',{'post':post})



    