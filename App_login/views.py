from django.contrib.auth import forms
from django.http import request
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_login.forms import SignUpForm,ProfileChange,ProfilePic
# Create your views here.


def signup(request):

    form= SignUpForm()
    registerd=False
    if request.method=="POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registerd=True
    dict={'form':form,'registerd':registerd}
    return render(request,'App_login/sign_up.html' ,context=dict)

def log_in(request):
    form = AuthenticationForm()
    if request.method=="POST":
        #please dont forget to make object of authentication form
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():

            user_name= form.cleaned_data.get('username')
            pass_word= form.cleaned_data.get('password')
            user=authenticate(username=user_name,password=pass_word)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))      

    return render(request,'App_login/login.html',context={'form':form})

@login_required
def log_out(request):
    logout(request)
    return(HttpResponseRedirect(reverse("App_login:signin")))

@login_required
def profile(request):


    return render(request,"App_login/profile.html",context={})

@login_required
def ChangeProfile(request):
    current_user=request.user
    form=ProfileChange(instance=current_user)
    if request.method=='POST':
        form=ProfileChange(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            #for updating profile
            form=ProfileChange(instance=current_user)
            
    return render(request,"App_login/Profile_change.html",context={'form':form})

@login_required
def changePassword(request):
    change=False
    current_user=request.user
    form=PasswordChangeForm(current_user)
    if request.method=='POST':
        form=PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            change=True

    return render(request,"App_login/passChange.html",context={'form':form, 'change':change})

@login_required
def profilePics(request):
    form=ProfilePic()
    if request.method=="POST":
     form=ProfilePic(request.POST,request.FILES)
     if form.is_valid():
         user_obj=form.save(commit=False)
         user_obj.user=request.user
         user_obj.save()
         return HttpResponseRedirect(reverse("App_login:profile"))

    return render(request,"App_login/profile_pic.html",context={"form":form})