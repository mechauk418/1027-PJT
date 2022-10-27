from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:reviews_pk>/', views.detail, name='detail'),
]
