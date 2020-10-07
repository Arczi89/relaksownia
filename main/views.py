from django.shortcuts import render

from .models import ContainerItem, SliderItem, SliderConfiguration


def main(request):
    containers = ContainerItem.objects.all()
    try:
        slider_configuration = SliderConfiguration.objects.all()[:1].get()
    except SliderConfiguration.DoesNotExist:
        slider_configuration = None
    slider_items = SliderItem.objects.all()
    context = {
        'containers': containers,
        'slider_items': slider_items,
        'slider_configuration': slider_configuration
    }
    return render(request, 'main.html', context)
