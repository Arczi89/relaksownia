from django.urls import reverse_lazy

from demosite.constants import field_required_and_invalid
from main.models import MainConfiguration
from .forms import NewsletterForm
from bootstrap_modal_forms.generic import BSModalCreateView


class NewsletterView(BSModalCreateView):
    template_name = 'newsletter.html'
    form_class = NewsletterForm
    success_message = 'Sukces!'
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['newsletterConfiguration'] = MainConfiguration.objects.all()[:1].get()
        except MainConfiguration.DoesNotExist:
            context['newsletterConfiguration'] = MainConfiguration
        context['field_required_and_invalid'] = field_required_and_invalid
        return context
