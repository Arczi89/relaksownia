from random import seed, randint

from django.core.management.base import BaseCommand

from opinions.models import OpinionItem


class Command(BaseCommand):
    help = 'Get reviews from google api'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        opinion_list = OpinionItem.objects.order_by("element_order")
        seed(1)
        position = 0
        for opinion in opinion_list:
            position = position + randint(0, 5)
            opinion.element_order = position
            opinion.save()
            self.stdout.write(self.style.SUCCESS("-----------"))
            self.stdout.write(self.style.SUCCESS(str(opinion.element_order) + ". " +opinion.customer_name + ":"))
            self.stdout.write(self.style.SUCCESS(opinion.opinion_text))

