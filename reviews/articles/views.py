import imp
from symbol import arith_expr
from django.shortcuts import render, redirect
from .models import Article, Comment
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)