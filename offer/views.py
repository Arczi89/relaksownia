from django.shortcuts import render

from .models import OfferItem


def offer(request):
    offers = OfferItem.objects.order_by("element_order")
    context = {
        'offers': offers
    }
    return render(request, 'offer.html', context)
