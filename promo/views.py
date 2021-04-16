from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from post_office import mail

from .forms import PromoClientForm
from .models import PromoPageComponent, PromoConfiguration, PromoEmailConfiguration


def promo(request):
    if request.method == "POST":
        form = PromoClientForm(request.POST)
        if form.is_valid():
            form.save()
            send_email_message(form)
            messages.add_message(request, messages.SUCCESS, 'Twoja wiadomość została wysłana.')
            return HttpResponseRedirect('/promo/')
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


def send_email_message(form):
    try:
        config = PromoEmailConfiguration.objects.all()
        email_configuration = config[:1].get()
    except PromoEmailConfiguration.DoesNotExist:
        email_configuration = PromoEmailConfiguration()

    if form['email'].data:
        mail.send(
            [form['email'].data],  # List of email addresses also accepted
            email_configuration.from_email,
            template='potwierdzenie_zamowienia',
            priority='now',
            context={
                'imie_i_nazwisko': form['contact_name'].data,
                'telefon': form['phone'].data,
                'ulica': form['street'].data,
                'kod_pocztowy': form['postcode'].data,
                'miasto': form['city'].data,
                'kod_inpost': form['inpost_code'].data,
                'miejsce_dostawy': form['delivery_place'].data,
                'firma': form['company_name'].data,
                'nip': form['nip'].data
            }
        )

    # if form['email'].data:
    #     send_mail(
    #         subject=email_configuration.subject,
    #         message=email_configuration.message,
    #         html_message=email_configuration.message,
    #         from_email=email_configuration.from_email,
    #         recipient_list=[form['email'].data],
    #         fail_silently=False,
    #     )


