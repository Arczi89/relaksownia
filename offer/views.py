from django.shortcuts import render

from .models import OfferItem, OfferConfiguration


def offer(request):
    offers = OfferItem.objects.all()
    configuration = OfferConfiguration.objects.all()[:1].get()
    context = {
        'offers': offers,
        'configuration': configuration
    }
    return render(request, 'offer/offer.html', context)
