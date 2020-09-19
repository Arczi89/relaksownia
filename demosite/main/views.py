from django.shortcuts import render

from .models import ContainerItem, SliderItem


def main(request):
    containers = ContainerItem.objects.all()
    slider_items = SliderItem.objects.all()
    context = {
        'containers': containers,
        'slider_items': slider_items
    }
    return render(request, 'main/main.html', context)
