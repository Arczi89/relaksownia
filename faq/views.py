from django.shortcuts import render

from .models import FaqItem, FaqConfiguration


def faq(request):
    faqs = FaqItem.objects.all()

    try:
        configuration = FaqConfiguration.objects.all()[:1].get()
    except FaqConfiguration.DoesNotExist:
        configuration = None

    context = {
        'faqs': faqs,
        'configuration': configuration
    }
    return render(request, 'faq.html', context)
