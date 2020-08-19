from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone


def home(request):
    post = Post.objects
    return render(request,'post/home.html',{'post':post})

@login_required(login_url="/account/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['post'] :
            post= Post()
            post.title = request.POST['title']
            post.body = request.POST['post']
            post.pub_date = timezone.datetime.now()
            post.smith = request.user
            post.save()
            return redirect('/post/' + str(post.id))
        else:
            return render(request,'post/create.html',{'error':'All fields are required'})
    else:
        return render(request,'post/create.html')

def detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request,'post/detail.html',{'post':post})

@login_required(login_url="/account/signup")
def upvote(request,post_id):
    if request.method == 'POST':
        post=get_object_or_404(Post,pk=post_id)
        post.votes_total.add(request.user)
        post.save()
        return redirect('home')
