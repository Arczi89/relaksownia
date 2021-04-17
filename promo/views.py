import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from post_office import mail
from post_office.mail import logger

from .forms import PromoClientForm
from .models import PromoPageComponent, PromoConfiguration, PromoEmailConfiguration, DeliveryKind


def promo(request):
    if request.method == "POST":
        form = PromoClientForm(request.POST)
        if form.is_valid():
            form.save()
            is_sent = send_email_to_customer(form)
            send_email_to_admin(form)
            show_status_message(is_sent, request)
            return HttpResponseRedirect('/promo/')
    else:
        form = PromoClientForm()

    promo_items = PromoPageComponent.objects.order_by("element_order")
    context = {
        'promoItems': promo_items,
        'form': form,
        'promo_configuration': get_promo_configuration()
    }
    return render(request, 'promo.html', context)


def get_promo_configuration():
    try:
        promo_configuration = PromoConfiguration.objects.all()[:1].get()
    except PromoConfiguration.DoesNotExist:
        promo_configuration = PromoConfiguration()
    return promo_configuration


def show_status_message(is_sent, request):
    if is_sent:
        messages.add_message(request, messages.SUCCESS, 'Twoja wiadomość została wysłana.')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Wysyłanie twojej wiadomości się nie powiodło. Skontaktuj się bezpośrednio pod adres: ' + get_email_configuration().from_email
        )


def send_email_to_customer(form):
    recipient = form['email'].data
    if recipient:
        mail.send(
            [recipient],
            sender=get_email_configuration().from_email,
            template=determine_template_name(form),
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
        return True
    else:
        logger.error("Wiadomość nie została wysłana do klienta, dane klienta: " + json.dumps(form))
        return False


def determine_template_name(form):
    if form['delivery_kind'].data == DeliveryKind.get_value('INPOST'):
        template_name = 'potwierdzenie_zamowienia_inpost'
    else:
        template_name = 'potwierdzenie_zamowienia_kurier'
    return template_name


def get_email_configuration():
    try:
        config = PromoEmailConfiguration.objects.all()
        email_configuration = config[:1].get()
    except PromoEmailConfiguration.DoesNotExist:
        email_configuration = PromoEmailConfiguration()
    return email_configuration


def send_email_to_admin(form):
    recipient = form['email'].data
    if recipient:
        mail.send(
            [get_email_configuration().admin_email],
            sender=get_email_configuration().from_email,
            template='potwierdzenie_zamowienia_admin',
            priority='now',
            context={
                'email_klienta': form['email'].data,
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
    else:
        logger.error("Wiadomość nie została wysłana do admina, dane klienta: " + json.dumps(form))
