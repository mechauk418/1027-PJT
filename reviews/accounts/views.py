from django.shortcuts import render,redirect, get_object_or_404
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    users = User.objects.all()
    content = {
        'users': users
    }
    return render(request,'accounts/index.html', content)

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
                return redirect(request.GET.get('next') or 'articles:index' )
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

@login_required
def update(request):

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')

    else:
        form = CustomUserChangeForm(instance = request.user)
    context={
        'form':form
    }

    return render(request,'accounts/update.html',context)

def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        return redirect('accounts:profile', pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect('accounts:profile', pk)