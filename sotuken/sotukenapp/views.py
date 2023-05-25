from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import SotukenModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html') 

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        address = request.POST['address']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, address, password)
            return render(request,'signup.html', {'some':100})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーはすでに登録されています。'})
    return render(request, 'signup.html')

@login_required
def homefunc(request):
    object_home = SotukenModel.objects.all()
    return render(request, 'home.html',{'object_home':object_home})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = get_object_or_404(SotukenModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
    object = SotukenModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('home')

def readfunc(request, pk):
    object = SotukenModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('home')
    else:
        object.read = object.read + 1
        object.readtext = object.readtext + ' ' + username
        object.save()
        return redirect('home')

class SotukenCreate(CreateView):
    template_name = 'create.html'
    model = SotukenModel
    fields = ('title', 'content', 'author', 'snsimage')
    success_url = reverse_lazy('home')

def mypagefunc(request):
    return render(request, 'mypage.html', {'object':object})