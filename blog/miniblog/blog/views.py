from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from turtle import update
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
SetPasswordForm
from .forms import  LoginForm, PostForm, singupForm
from django.contrib.auth.models import User,Group
from .models import Post
# Create your views here.
#for home
def HomePage(request):
    posts = Post.objects.all()
    return render(request,"blog/home.html",{'posts':posts})

#for singup
def user_singup(request):
    if request.method=="POST":
        form = singupForm(request.POST)
        if form.is_valid():
            messages.success(request,"succesfully save...")
            form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            form = singupForm()
            print("succesfully save...") 
    else:
        form = singupForm
    return render(request,'blog/singup.html',{'form':form})

#for user_login
def user_Login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            user = LoginForm(request=request, data=request.POST)
            if user.is_valid():
                u_name = user.cleaned_data['username']
                u_pass = user.cleaned_data['password']
                fm = authenticate(username=u_name, password=u_pass)
                if fm is not None:
                    login(request, fm)
                    messages.success(request,"Login succesfully...")
                    return HttpResponseRedirect("/dashbord")
        else:
            user = LoginForm()
        return render(request,"blog/login.html",{'form':user})
    else:
        return HttpResponseRedirect('/dashbord')

#for about
def About(request):
    return render(request,'blog/about.html')

# for dashbord
def Dashbord(request):
    if  request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'blog/dashbord.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login')

#for navbarr
def navbar(request):
    return render(request,"blog/navbar.html")

# for Contact
def Contact(request):
    return render(request,"blog/contact.html")

#for logout
def user_Logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

#add new post
def add_post(request):
    if  request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                decs = form.cleaned_data['decs']
                pst = Post(title=title,decs=decs)
                pst.save()
                return HttpResponseRedirect("/dashbord")
        else:
            form = PostForm()
            return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect("/login")

#update post
def update_post(request,id):
    if  request.user.is_authenticated:
        if request.method=="POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                messages.success(request,"succesfully updated...")
                form.save()
                form = PostForm()
                return HttpResponseRedirect("/dashbord")
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'blog/updatePost.html',{'form':form})
       
    else:
        return HttpResponseRedirect("/login")
    
#delete post
def delete_post(request):
    if request.user.is_authenticted:
        return HttpResponseRedirect("/dashbord")
    else:
        return HttpResponseRedirect("/login")