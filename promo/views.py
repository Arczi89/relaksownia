from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import PromoClientForm
from .models import PromoPageComponent


def promo(request):
    if request.method == "POST":
        form = PromoClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Twoja wiadomość została wysłana.')
            return HttpResponseRedirect('/contact/')
    else:
        form = PromoClientForm()

    promo_items = PromoPageComponent.objects.order_by("element_order")
    context = {
        'promoItems': promo_items,
        "form": form
    }
    return render(request, 'promo.html', context)
