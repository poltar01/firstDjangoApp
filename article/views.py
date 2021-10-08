from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models import Article,Comment
from .forms import ArticleForm
from django.contrib import messages
from django.http import request
from django.contrib.auth.decorators import login_required
from user.models import userInfo
# Create your views here.

def index(request):


    if request.user.is_authenticated:
        user_info = request.user.userinfo

        return render(request,"index.html",{"user_info" : user_info})
    else:
        return render(request,"index.html")


def about(request):

    if request.user.is_authenticated:
        user_info = request.user.userinfo
        context={
            "user_info" : user_info
        }
        return render(request,"about.html",context)
    else:
        return render(request,"about.html")


def detail(request,id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()


    for comment in comments:
        user = userInfo.objects.get(username = comment.comment_author)
        comment.comment_author_image_url = user.profile_image.url
        comment.save()
        print(comment.comment_author_image_url)
        


    if request.user.is_authenticated:

        user_info = request.user.userinfo
        context = {
            "article" : article,
            "comments" : comments,
            "user_info" : user_info
        }
    else:
        context = {
            "article" : article,
            "comments" : comments,
        }

    return render(request,"detail.html",context)


@login_required(login_url="user:loginUser")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)


    user_info = request.user.userinfo
    context = {
        "articles" : articles,
        "user_info" : user_info
    }
    return render(request,"dashboard.html",context)


@login_required(login_url="user:loginUser")
def addArticle(request):


    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()
        

        messages.success(request, "Yeni Makale Eklendi, "+request.user.username+".")
    
        return redirect("article:dashboard")
        #articles.html yada dashboard yapılıp renderlanacak/*redirect olacaK!*    de olabilir..
    

    user_info = request.user.userinfo

    context = {
        "form" : form,
        "user_info" : user_info
    }
    

    return render(request,"addArticle.html",context)


@login_required(login_url="user:loginUser")
def updateArticle(request,id):
    
    article = get_object_or_404(Article,id = id)

    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user # KALDIRILABİLİR 
        article.save()
        

        messages.success(request, "Makale Güncellendi, "+request.user.username+".")
    
        return redirect("article:dashboard")
        #articles.html yada dashboard yapılıp renderlanacak/*redirect olacaK!*    de olabilir..
    

    user_info = request.user.userinfo
    context = {
        "form" : form,
        "user_info" : user_info,
    }
    

    return render(request,"update.html",context)

@login_required(login_url="user:loginUser")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()

    messages.warning(request, "Makale Kaldırıldı, "+request.user.username+".")


    user_info = request.user.userinfo
    return redirect("article:dashboard")



def articles(request):
    
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        if request.user.is_authenticated:
            user_info = request.user.userinfo
            context={
                "articles": articles,
                "user_info" : user_info
            }
        else:
            context={
                "articles": articles
            }
        return render(request,"articles.html",context)

    articles = Article.objects.filter()
    
    
    if request.user.is_authenticated:
        user_info = request.user.userinfo
        context={
            "articles": articles,
            "user_info" : user_info
        }
    else:
        context={
            "articles": articles
        }
        
    
    return render(request,"articles.html",context)



@login_required(login_url="user:loginUser")
def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    if request.method == "POST":
        comment_author = request.user.username
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author,comment_content = comment_content)

        newComment.article = article
        newComment.save()



    return redirect(reverse("article:detail", kwargs = {"id":id}))