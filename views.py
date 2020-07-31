from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def register(request):
    if request.user.is_authenticated:#if user do login and get left then open timetable creation page
        return redirect('time')
    else:
        form=UserCreationForm
        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("login")

    params={'form':form}
    return render(request,'timezone/register.html',params)
def loginp(request):
    if request.user.is_authenticated:
        return redirect('time')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('time')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'timezone/login.html', context)
def time(request):
    return render(request,"timezone/timetable.html")
def logoutuser(request):
    logout(request)
    return redirect('login')