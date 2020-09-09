from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def contact(request):
    return render(request, 'contact.html')


def contact_send_message(request):
    # TODO+ obsłużyć formularz
    return HttpResponseRedirect(reverse('main'))
