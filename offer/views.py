from django.shortcuts import render

from .models import OfferItem, OfferConfiguration


def offer(request):
    offers = OfferItem.objects.all()
    try:
        configuration = OfferConfiguration.objects.all()[:1].get()
    except OfferConfiguration.DoesNotExist:
        configuration = None
    context = {
        'offers': offers,
        'configuration': configuration
    }
    return render(request, 'offer.html', context)
