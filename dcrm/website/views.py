from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Records
# Create your views here.
@login_required(login_url='login')
def home(request):
    records=Records.objects.all()
    return render(request, 'home.html',{'records':records})
def login_user(request):
    # check to see logged or not
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #authenticate 
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user) 
            messages.success(request,"You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"Wrong Password or Username please try again")
            return redirect("login")
    else:
        return render(request,'login.html')

def logout_user(request): 
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect("login")


def register_user(request):
    if request.method=='POST': 
        form=SignUpForm(request.POST)
        if form.is_valid(): 
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"Registration Successful")
            return redirect('home')
        
        
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Records.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must be Logged in")
        return redirect('login')
    

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Records.objects.get(id=pk)
        messages.success(request,"Record Deleted")
        delete_it.delete()
        return redirect('home')
    else:
        messages.success(request,"You must have to login to delete")
        return redirect('login')
    

def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                form.save()
                messages.success(request,"Record added")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in")
        return redirect('login')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Records.objects.get(id=pk)
        form=AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,'you must be logged in')
        return redirect('login')
