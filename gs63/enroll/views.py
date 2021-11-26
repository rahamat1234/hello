from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
#### Signup  function ke liy ye form hai
def sign_up(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Create Successfully !!')
            fm.save()
    else:
        fm=SignUpForm()
    return render(request,'enroll/signup.html',{'form':fm})

    # Login Views Function ke liy form hai
def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render(request, 'enroll/userlogin.html', {'form':fm})

############# Profile Function 

def user_profile(request):
    return render(request, 'enroll/profile.html')




