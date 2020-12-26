from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.models import MainConfiguration
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
        messages.add_message(request, messages.SUCCESS, 'Zostałeś dodany do listy newslettera.')
        return HttpResponseRedirect(reverse('faq'))
