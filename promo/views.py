from django.shortcuts import render

from .models import PromoItem


def promo(request):
    promo_items = PromoItem.objects.all()
    context = {
        'promoItems': promo_items
    }
    return render(request, 'promo.html', context)
