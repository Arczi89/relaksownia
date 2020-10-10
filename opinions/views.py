from django.shortcuts import render

from .models import OpinionsConfiguration, OpinionItem


def opinions(request):
    try:
        configuration = OpinionsConfiguration.objects.all()[:1].get()
    except OpinionsConfiguration.DoesNotExist:
        configuration = None

    opinions = OpinionItem.objects.all()
    context = {
        'configuration': configuration,
        'opinions': opinions
    }
    return render(request, 'opinions.html', context)
