from django.shortcuts import render

from .models import BlogPost


def blog(request):
    blog_posts = BlogPost.objects.all()
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blog/blog.html', context)
