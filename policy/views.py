from django.shortcuts import render

from .models import PolicyConfiguration


def blog(request):
    try:
        configuration = PolicyConfiguration.objects.all()[:1].get()
    except PolicyConfiguration.DoesNotExist:
        configuration = None

    context = {
        'configuration': configuration,
    }
    return render(request, 'policy.html', context)
