from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)

def single_view(request,pid):
    post = get_object_or_404(Post,pk=pid,status=1)
    context = {'post' : post}
    return render(request,'blog/blog-single.html',context)

def next_previous(request):
    posts = Post.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'index.html', context)