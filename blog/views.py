from django.shortcuts import render

from .models import BlogConfiguration, BlogPost


def blog(request):
    try:
        configuration = BlogConfiguration.objects.all()[:1].get()
    except BlogConfiguration.DoesNotExist:
        configuration = None

    blog_posts = BlogPost.objects.all()
    context = {
        'configuration': configuration,
        'blog_posts': blog_posts
    }
    return render(request, 'blog.html', context)
