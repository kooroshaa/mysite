from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)

def single_view(request):
    return render(request,'blog/blog-single.html')

