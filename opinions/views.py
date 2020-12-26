from django.shortcuts import render

from .models import OpinionsConfiguration, OpinionItem, OpinionTreeItem


def opinions(request):
    try:
        configuration = OpinionsConfiguration.objects.all()[:1].get()
    except OpinionsConfiguration.DoesNotExist:
        configuration = None

    opinion_list = OpinionItem.objects.order_by("element_order")
    opinion_tree = OpinionTreeItem.objects.order_by("element_order")
    context = {
        'configuration': configuration,
        'opinions': opinion_list,
        'opinion_tree': opinion_tree
    }
    return render(request, 'opinions.html', context)
