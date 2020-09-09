from django.shortcuts import render

from .models import ContainerItem


def index(request):
    containers = ContainerItem.objects.all()
    context = {
        'containers': containers
    }
    return render(request, 'index.html', context)
