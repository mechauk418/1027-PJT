from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        "article": article,
        'comment_form': CommentForm(),
        'comment': article.comment_set.all(),
    }
    return render(request, "articles/detail.html", context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/forms.html", context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect("articles:detail", article_pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
    }
    return render(request, "articles/forms.html", context)


# @login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect("articles:detail", article.pk)
    return redirect("articles:detail", article.pk)


# @login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        if request.method == "POST":
            comment.delete()
            return redirect("articles:detail", article_pk)
    return redirect("articles:detail", article_pk)


# @login_required
def like(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(id=request.user.id).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect("articles:detail", article_pk)
