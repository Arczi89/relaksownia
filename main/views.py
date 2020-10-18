from django.shortcuts import render

from .models import MainBoxItem, MainSliderItem, MainSliderConfiguration, MainConfiguration


def main(request):
    containers = MainBoxItem.objects.all()
    try:
        slider_configuration = MainSliderConfiguration.objects.all()[:1].get()
    except MainSliderConfiguration.DoesNotExist:
        slider_configuration = None

    try:
        configuration = MainConfiguration.objects.all()[:1].get()
    except MainConfiguration.DoesNotExist:
        configuration = None

    slider_items = MainSliderItem.objects.all()
    context = {
        'containers': containers,
        'slider_items': slider_items,
        'slider_configuration': slider_configuration,
        'configuration': configuration
    }
    return render(request, 'main.html', context)