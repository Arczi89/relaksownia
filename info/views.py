from django.shortcuts import render

from .models import Info


def info(request):
    try:
        about_me = Info.objects.all()[:1].get()
    except Info.DoesNotExist:
        about_me = None
    context = {
        'about_me': about_me
    }
    return render(request, 'info.html', context)
