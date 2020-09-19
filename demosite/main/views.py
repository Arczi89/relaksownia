from django.shortcuts import render

from .models import ContainerItem, SliderItem, Info


def main(request):
    containers = ContainerItem.objects.all()
    slider_items = SliderItem.objects.all()
    if Info.objects.count != 0:
        info = Info.objects.all()[:1].get()
    context = {
        'containers': containers,
        'slider_items': slider_items,
        'info': info
    }
    return render(request, 'main/main.html', context)
