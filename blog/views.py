from django.shortcuts import render

from .models import BlogConfiguration


def blog(request):
    try:
        configuration = BlogConfiguration.objects.all()[:1].get()
    except BlogConfiguration.DoesNotExist:
        configuration = None
    context = {
        'configuration': configuration
    }
    return render(request, 'blog.html', context)
