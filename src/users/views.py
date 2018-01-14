from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm, NewUserForm

# Create your views here.
class LoginView(View):
    def get(self,request):
        context = {'form':LoginForm}
        return render(request,"login_form.html",context)

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login_username')
            password = form.cleaned_data.get('login_password')
            authenticated_user = authenticate(username=username,password=password)
            if authenticated_user and authenticated_user.is_active:
                django_login(request,authenticated_user)
                redirect_to = request.GET.get('next','home_page')
                return redirect(redirect_to)
            else:
                messages.error(request,message='usuario incorrecto')
        return render(request,"login_form.html",{'form':form})

def logout(request):
    django_logout(request)
    return redirect('login_page')

class CreateUser(View):
    def get(self,request):
        context = {'form':NewUserForm}
        return render(request,"signup_page.html",context)

    def post(self,request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            form = NewUserForm
            messages.success(request,"Usuario creado")
        return render(request,"signup_page.html",{"form":form})
