from django.shortcuts import render,redirect, get_object_or_404
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model

# Create your views here.

def index(request):

    return render(request,'accounts/index.html')

def signup(request):

    if request.method=='POST':
        
        signup_form = CustomUserCreationForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()

            return redirect('accounts:index')

    else:
        signup_form = CustomUserCreationForm()

    context = {
        'signup_form' : signup_form,
    }

    return render(request,'accounts/signup.html',context)

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request,data=request.POST)

            if login_form.is_valid():
                auth_login(request,login_form.get_user()
                )
                return redirect(request.GET.get('next') or 'accounts:index' )
        else:
            login_form = AuthenticationForm()

        context = {
            'login_form':login_form
        }
        return render(request,'accounts/login.html',context)

    else:
        return redirect('accounts:index')

def logout(request):
    auth_logout(request)

    return redirect('accounts:index')

def profile(request,pk):

    user = get_object_or_404(get_user_model(), pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        return redirect('accounts:profile', pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect('accounts:profile', pk)

# @require_POST
# def follow(request,pk):
#     if request.user.is_authenticated:
#         User = get_user_model()
#         me = request.user
#         you = User.objects.get(pk=pk)

#         if me != you:
#             if you.followers.filter(pk=me.pk).exists():
#                 you.followers.remove(me)
#                 is_followed = False

#             else:
#                 you.followers.add(me)
#                 is_followed = True

#             context = {
#                 'is_follow':is_followed,
#             }
#             return JsonResponse(context)

#         return redirect('accounts:profile',you.username)
#     return redirect('accounts:login')
