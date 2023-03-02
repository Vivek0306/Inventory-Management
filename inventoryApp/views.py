from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json, sys
from datetime import date, datetime
from .models import Category, Products
# Create your views here.

# Login
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required
def home(request):
    now = datetime.now()
    categories = len(Category.objects.all())
    products = len(Products.objects.all())
    context = {
        'categories' : categories,
        'products' : products,
    }
    return render(request, 'home.html', context)

#  Categories
@login_required
def category(request):
    category_list = Category.objects.all()
    context = {
        'page_title' : 'Category List',
        'category' : category_list,
    }
    return render(request, 'category.html', context)