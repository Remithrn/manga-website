from django.shortcuts import render,redirect
from .models import Books
from . forms import BooksForm,RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages

# Create your views here.
def home_page(request):
    books=Books.objects.all()
    return render(request,'blogapp/index.html',{'books':books})


@login_required(login_url='login')
@never_cache
def create(request):
    form=BooksForm()
    if request.method =="POST":
        form=BooksForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request,"successful!!")
            return redirect('home')
    return render(request,'blogapp/create.html',{'form':form})


def details(request,id):
    book=Books.objects.get(id=id)
    return render(request,'blogapp/detail.html',{'book':book})


@never_cache
@login_required(login_url='login')
def update_details(request,id):    
    book=Books.objects.get(id=id)
    form=BooksForm(instance=book)
    if request.method =='POST':
        form = BooksForm(request.POST,request.FILES,instance=book)
        if form.is_valid:
            form.save()
            messages.success(request,"successful!!")
            return redirect('home')
    return render(request,'blogapp/create.html',{'form':form,'book':book})


@login_required(login_url='login')
@never_cache
def delete_book(request,id):
    book=Books.objects.get(id=id)
    book.delete()
    messages.success(request,"successful!!")
    return redirect('home')

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"successful!!")
            return redirect('home')
        else:
            messages.error(request,"incorrrect username or password ,try again")
            return render(request,'blogapp/login.html')
    return render(request,'blogapp/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"logged out")
    return redirect('home')


def register_user(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully created an account")
            return redirect('login')
        else:
            form=RegistrationForm(request.POST)
            messages.error(request,"incorrect data")
            return render(request,'blogapp/register.html',{'form':form})

    return render(request,'blogapp/register.html',{'form':form})


def contact(request):
    return render(request,'blogapp/contact.html')

def about(request):
    return render(request,'blogapp/about.html')

