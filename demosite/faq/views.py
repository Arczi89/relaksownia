from django.shortcuts import render


def faq(request):
    context = {}
    return render(request, 'faq/faq.html', context)
