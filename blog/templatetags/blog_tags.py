from django import template
from blog.models import Post,Category

register = template.Library()

@register.inclusion_tag('blog/blog-popular-posts.html')
def latastposts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:2]
    return {'posts' : posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    return {'categories' : cat_dict}

