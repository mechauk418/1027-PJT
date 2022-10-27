from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

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
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/forms.html', context)
    
def update(request,review_pk):
    article = Article.objects.get(pk=review_pk)
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect('articles:detail', review_pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
    }
    return render(request, 'articles/forms.html', context)