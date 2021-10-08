from django.contrib import admin
from django.urls import path,include
from . import views

app_name="article"
urlpatterns = [
    path('create/',views.index,name = "create"),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addArticle"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "updateArticle"),
    path('delete/<int:id>',views.deleteArticle,name = "deleteArticle"),
    path('',views.articles,name = "articles"),
    path('comment/<int:id>',views.addComment,name = "comment"),
]