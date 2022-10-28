from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/update/', views.update, name='update'),
    path('search/', views.search, name='search'),
]
