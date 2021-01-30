from django.shortcuts import render

from .models import PromoItem


def promo(request):
    promo_items = PromoItem.objects.order_by("element_order")
    context = {
        'promoItems': promo_items
    }
    return render(request, 'promo.html', context)
