from django.shortcuts import render

from .models import Info, CertItem


def info(request):
    try:
        about_me = Info.objects.all()[:1].get()
    except Info.DoesNotExist:
        about_me = None
    try:
        certs = CertItem.objects.order_by('element_order')
    except CertItem.DoesNotExist:
        certs = None

    context = {
        'about_me': about_me,
        'certs': certs
    }
    return render(request, 'info.html', context)
