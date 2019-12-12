from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from .forms import *

def p(request):
    posts = Python.objects.all()
    return render(request, 'python.html', {'posts': posts})

def j(request):
    posts = Python.objects.all()
    return render(request, 'Java.html', {'posts': posts})

def php(request):
    posts = Python.objects.all()
    return render(request, 'PHP.html', {'posts': posts})

def csharp(request):
    posts = Python.objects.all()
    return render(request, 'C#.html', {'posts': posts})

def cplus(request):
    posts = Python.objects.all()
    return render(request, 'C++.html', {'posts': posts})

def c(request):
    posts = Python.objects.all()
    return render(request, 'C.html', {'posts': posts})


def ruby(request):
    posts = Python.objects.all()
    return render(request, 'Ruby.html', {'posts': posts})

def electrical(request):
    posts = Python.objects.all()
    return render(request, 'Electrical.html', {'posts': posts})

def electronics(request):
    posts = Python.objects.all()
    return render(request, 'Electronics.html', {'posts': posts})

def civil(request):
    posts = Python.objects.all()
    return render(request, 'Civil.html', {'posts': posts})

def mechanical(request):
    posts = Python.objects.all()
    return render(request, 'Mechanical.html', {'posts': posts})








