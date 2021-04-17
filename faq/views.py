from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from post_office.mail import logger
from post_office import mail

from main.models import MainConfiguration
from promo.models import PromoEmailConfiguration
from .forms import NewsletterFaqForm
from .models import FaqItem, FaqConfiguration


def faq(request):
    faqs = FaqItem.objects.order_by('element_order')
    try:
        configuration = FaqConfiguration.objects.all()[:1].get()
        newsletter_configuration = MainConfiguration.objects.all()[:1].get()
    except (FaqConfiguration.DoesNotExist, MainConfiguration.DoesNotExist):
        configuration = None
        newsletter_configuration = None
    if request.method == "POST":
        saveForm(request)
        form = NewsletterFaqForm(request.POST)
    else:
        form = NewsletterFaqForm()
    context = {
        'faqs': faqs,
        'configuration': configuration,
        'newsletterConfiguration': newsletter_configuration,
        'form': form,
        'action': '/faq/'
    }
    return render(request, 'faq.html', context)


def store_newsletter_request(form):
    form.save()


def saveForm(request):
    form = NewsletterFaqForm(request.POST)
    if form.is_valid():
        store_newsletter_request(form)
        is_sent = send_email_to_customer(form)
        send_email_to_admin(form)
        show_status_message(is_sent, request)
        return HttpResponseRedirect(reverse('faq'))


def show_status_message(is_sent, request):
    if is_sent:
        messages.add_message(request, messages.SUCCESS, 'Zostałeś zapisany na newsletter, dostaniesz email potwierdzający.')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Wysyłanie twojej wiadomości się nie powiodło. Skontaktuj się bezpośrednio pod adres: ' + self.get_email_configuration().from_email
        )


def get_email_configuration():
    try:
        config = PromoEmailConfiguration.objects.all()
        email_configuration = config[:1].get()
    except PromoEmailConfiguration.DoesNotExist:
        email_configuration = PromoEmailConfiguration()
    return email_configuration


def send_email_to_customer(form):
    recipient = form['email'].data
    if recipient:
        mail.send(
            [recipient],
            sender=get_email_configuration().from_email,
            template="potwierdzenie_newsletter",
            priority='now',
            context={
                'imie': form['name'].data,
                'email': form['email'].data,
            }
        )
        return True
    else:
        logger.error("Wiadomość nie została wysłana do klienta, dane klienta: " + json.dumps(form))
        return False


def send_email_to_admin(form):
    recipient = form['email'].data
    if recipient:
        mail.send(
            [get_email_configuration().admin_email],
            sender=get_email_configuration().from_email,
            template='potwierdzenie_newsletter_admin',
            priority='now',
            context={
                'imie': form['name'].data,
                'email': form['email'].data,
            }
        )
    else:
        logger.error("Wiadomość nie została wysłana do admina, dane klienta: " + json.dumps(form))
