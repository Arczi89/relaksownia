from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import ContactConfiguration
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            store_contact_request(form)
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()

    context = {
        "configuration": get_configuration(),
        'form': form
    }

    return render(request, 'contact.html', context)


def get_configuration():
    try:
        configuration = ContactConfiguration.objects.all()[:1].get()
    except ContactConfiguration.DoesNotExist:
        configuration = None

    return configuration


def store_contact_request(form):
    print("zapisane")
    pass