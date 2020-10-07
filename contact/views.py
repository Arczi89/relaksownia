from django.shortcuts import render

from .models import ContactConfiguration

def contact(request):
    return render(request, 'contact.html', get_context_with_configuration())


def contact_send_message(request):
    # TODO+ obsłużyć formularz
    return render(request, 'contact.html', get_context_with_configuration())


def get_context_with_configuration():
    try:
        configuration = ContactConfiguration.objects.all()[:1].get()
    except ContactConfiguration.DoesNotExist:
        configuration = None

    context = {
        'configuration': configuration
    }
    return context