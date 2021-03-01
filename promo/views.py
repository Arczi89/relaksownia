from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import PromoClientForm
from .models import PromoPageComponent, PromoConfiguration


def promo(request):
    if request.method == "POST":
        form = PromoClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Twoja wiadomość została wysłana.')
            return HttpResponseRedirect('/contact/')
    else:
        form = PromoClientForm()

    try:
        promo_configuration = PromoConfiguration.objects.all()[:1].get()
    except PromoConfiguration.DoesNotExist:
        promo_configuration = PromoConfiguration()

    promo_items = PromoPageComponent.objects.order_by("element_order")
    context = {
        'promoItems': promo_items,
        'form': form,
        'promo_configuration': promo_configuration
    }
    return render(request, 'promo.html', context)
