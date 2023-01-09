from django.shortcuts import render
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts': posts}
    def blog_post(request, post_id):
        blog_object = Post.objects.get(id=post_id)
        blog_object.counted_views = blog_object.counted_views+1
        blog_object.save()

    return render(request, 'blog/blog-home.html', context)


def single_view(request):
    return render(request, 'blog/blog-single.html')
