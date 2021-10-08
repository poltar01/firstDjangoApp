from django import forms
from .models import Article
from django.http import request

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","image"]