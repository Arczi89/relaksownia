from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from post_office import mail
from post_office.mail import logger

from promo.models import PromoEmailConfiguration
from .models import ContactConfiguration
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            store_contact_request(form)
            is_sent = send_email_to_customer(form)
            send_email_to_admin(form)
            show_status_message(is_sent, request)
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()

    context = {
        "configuration": get_configuration(),
        "form": form
    }

    return render(request, 'contact.html', context)


def get_configuration():
    try:
        configuration = ContactConfiguration.objects.all()[:1].get()
    except ContactConfiguration.DoesNotExist:
        configuration = None

    return configuration


def store_contact_request(form):
    form.save()
    pass


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
            template='potwierdzenie_kontakt',
            priority='now',
            context={
                'imie': form['name'].data,
                'email_klienta': form['email'].data,
                'wiadomosc_klienta': form['message'].data,
            }
        )
        return True
    else:
        logger.error("Wiadomość nie została wysłana do klienta, dane klienta: " + form_to_string(form))
        return False


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
            template='potwierdzenie_kontakt_admin',
            priority='now',
            context={
                'imie': form['name'].data,
                'email_klienta': form['email'].data,
                'wiadomosc_klienta': form['message'].data,
            }
        )
    else:
        logger.error("Wiadomość nie została wysłana do admina, dane klienta: " + form_to_string(form))


def form_to_string(form):
    result = "{"
    for key, value in form.data.items():
        result += key + " : " + value + ", "
    result += "}"
    return result
