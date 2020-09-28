from django.shortcuts import render

from .models import FaqItem


def faq(request):
    faqs = FaqItem.objects.all()
    context = {
        'faqs': faqs
    }
    return render(request, 'faq/faq.html', context)
