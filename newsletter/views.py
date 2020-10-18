from django.urls import reverse_lazy
from .forms import NewsletterForm
from bootstrap_modal_forms.generic import BSModalCreateView

class NewsletterView(BSModalCreateView):
    template_name = 'newsletter.html'
    form_class = NewsletterForm
    success_message = 'Sukces!'
    success_url = reverse_lazy('main')