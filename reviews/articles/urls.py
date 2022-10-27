from django.urls import path

from reviews.articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
]
