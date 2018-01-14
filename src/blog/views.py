from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from django.urls import reverse

from django.views import View

from blog.forms import PostForm


@login_required
def home(request):
    return render(request,"home.html")


class CreatePost(View):
    def get(self,request):
        form = PostForm()
        return render(request,"post_form.html",{'form':form})
    def post(self,request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail.html",args=[post.pk]) #Tengo que crear esta vista - y su modelo.
            message = "Post creado con éxito :D"
            message += '<a href="{}">Ver Post</a>'.format(url)
            messages.success(request,message)
        return render(request,"post_form.html",{'form':form})
