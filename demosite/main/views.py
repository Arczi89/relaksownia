from django.shortcuts import render

from .models import ContainerItem


def main(request):
    containers = ContainerItem.objects.all()
    context = {
        'containers': containers
    }
    return render(request, 'main/main.html', context)
