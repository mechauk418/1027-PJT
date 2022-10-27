from django.shortcuts import render,redirect
from .models import User
from .forms import CustomUserCreationForm
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