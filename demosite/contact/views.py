from django.shortcuts import render


def contact(request):
    return render(request, 'contact.html')


def contact_send_message(request):
    # TODO+ obsłużyć formularz
    return render(request, 'contact.html')
