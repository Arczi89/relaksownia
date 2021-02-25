from django.shortcuts import render

from .models import PromoPageComponent


def promo(request):
    promo_items = PromoPageComponent.objects.order_by("element_order")
    context = {
        'promoItems': promo_items
    }
    return render(request, 'promo.html', context)
