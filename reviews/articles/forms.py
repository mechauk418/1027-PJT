from socket import fromshare
from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", 'grade', "image",]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
        widgets = {"content": forms.Textarea(attrs={"class": "from-control", 'rows': 1})}
        labels = {'content': '댓글',}