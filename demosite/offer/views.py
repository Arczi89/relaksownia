from django.shortcuts import render


def offer(request):
    context = {}
    return render(request, 'offer/offer.html', context)
