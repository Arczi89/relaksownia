from django.shortcuts import render

from .models import OfferItem, OfferConfiguration


def offer(request):
    offers = OfferItem.objects.order_by("element_order")
    try:
        configuration = OfferConfiguration.objects.all()[:1].get()
    except OfferConfiguration.DoesNotExist:
        configuration = None
    context = {
        'offers': offers,
        'configuration': configuration
    }
    return render(request, 'offer.html', context)
