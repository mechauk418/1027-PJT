import imp
from symbol import arith_expr
from django.shortcuts import render, redirect

from reviews import articles
from .models import Article, Comment
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request,review_pk):
    article = Article.objects.get(pk=review_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html')