from django.shortcuts import render

from .models import OfferItem


def offer(request):
    offers = OfferItem.objects.all()
    context = {
        'offers': offers
    }
    return render(request, 'offer.html', context)
