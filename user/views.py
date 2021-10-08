from django.shortcuts import redirect, render,get_object_or_404
from .forms import RegisterForm,LoginForm,userInfoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from user.models import userInfo
from article.models import Article,Comment
from django.http import request
from django.contrib.auth.decorators import login_required


# Create your views here.

def registerUser(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        newUserInfo = userInfo(user = request.user,username = request.user.username)
        newUserInfo.save()

        messages.success(request, 'Hesabınız başarılı bir şekilde oluşturuldu.')
    
        return redirect("index")

    if request.user.is_authenticated:
        user_info = request.user.userinfo
    
        context = {
            "form" : form,
            "user_info" : user_info,
        }
    else:
        context = {
            "form" : form,
        }
    return render(request,"register.html",context)

def loginUser(request):

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        User = authenticate(request,username = username,password = password)
        if User is not None:
            login(request,User)

            messages.success(request, "Giriş yapıldı, "+request.user.username+".")
    
            return redirect("index")
        else:
            
            messages.warning(request, 'Böyle bir kullanıcı bulunamadı.')
            return redirect("loginUser")

    if request.user.is_authenticated:
        user_info = request.user.userinfo
    
        context = {
            "form" : form,
            "user_info" : user_info,
        }
    else:
        context = {
            "form" : form,
        }
    
    return render(request,"login.html",context)


@login_required(login_url="user:loginUser")
def logoutUser(request):
    username = request.user.username
    logout(request)
    messages.warning(request,"Çıkış yapıldı, "+username+".")
    return redirect("index")


@login_required(login_url="user:loginUser")
def userProfile(request):
    
    user_info = request.user.userinfo
    user_comments = Comment.objects.filter(comment_author = request.user.username)
    user_articles = Article.objects.filter(author = request.user)

    comments_len = len(user_comments)
    articles_len = len(user_articles)
    context = {
        "user_info" : user_info,
        # "user_image" : user_image,
        "user_comments" : user_comments,
        "comments_len" : comments_len,
        "user_articles" : user_articles,
        "articles_len" : articles_len,
    }
    return render(request,"profile.html",context)

@login_required(login_url="user:loginUser")
def editProfile(request):


    userProfile = get_object_or_404(userInfo,user = request.user)

    form = userInfoForm(request.POST or None,request.FILES or None,instance=userProfile)
    if form.is_valid():
        user_profile = form.save(commit=False)
        
        user_profile.profile_image.thumbnail(320,320)
        user_profile.save()
        

        messages.success(request, "Profil Güncellendi, "+request.user.username+".")
    
        return redirect("article:dashboard")

    user_info = request.user.userinfo
    context={
        "form" : form,
        "user_info" : user_info
    }
    return render(request,"editProfile.html",context)