from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django import forms
from .models import Records
class SignUpForm(UserCreationForm): 
    email= forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'})) 
    first_name= forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))  


    class Meta: 
        model=User 
        fields=('username','first_name','last_name','email','password1','password2')


#adding record 
class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":'First Name','class':'form-control'}))
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":'Last Name','class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":'Email','class':'form-control'}))
    phone=forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":'Phone','class':'form-control'}))
    address=forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":'Address','class':'form-control'}))
    city=forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":'City','class':'form-control'}))
    state=forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":'State','class':'form-control'}))
    zipcode=forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":'Zipcode','class':'form-control'}))

    class Meta:
        model=Records
        exclude=("user",)