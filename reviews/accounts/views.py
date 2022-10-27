from django.shortcuts import render,redirect
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

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