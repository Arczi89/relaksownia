from django.shortcuts import render

from main.models import MainConfiguration
from newsletter.forms import NewsletterForm
from .models import FaqItem, FaqConfiguration


def faq(request):
    faqs = FaqItem.objects.all()

    try:
        configuration = FaqConfiguration.objects.all()[:1].get()
        newsletter_configuration = MainConfiguration.objects.all()[:1].get()
    except FaqConfiguration.DoesNotExist:
        configuration = None
    except MainConfiguration.DoesNotExist:
        configuration = None
    context = {
        'faqs': faqs,
        'configuration': configuration,
        'newsletterConfiguration': newsletter_configuration,
        'form': NewsletterForm
    }
    return render(request, 'faq.html', context)
