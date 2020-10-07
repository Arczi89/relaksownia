from django.shortcuts import render


def opinions(request):
    context = {}
    return render(request, 'opinions.html', context)
