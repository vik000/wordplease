from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.urls import reverse

from django.views import View

from blog.forms import PostForm
from blog.models import Post


@login_required
def home(request):
    latest_posts = Post.objects.all().order_by('postDate')
    context = {'posts':latest_posts}
    return render(request,"home.html",context)

@login_required
def post_detail(request,pk):
    post_selection = Post.objects.filter(pk=pk)
    if len(post_selection == 0):
        return render(request,"404.html",status=404)
    else:
        post = post_selection[0]
        context = {'post':post}
        return render(request,"post_detail_page.hmtl",context)

@login_required
def all_blogs(request):
    pass



class CreatePost(LoginRequiredMixin,View):
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
