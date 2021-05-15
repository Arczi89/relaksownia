from django.contrib import messages
from django.urls import reverse_lazy
from post_office import mail
from post_office.mail import logger

from demosite.constants import field_required_and_invalid
from main.models import MainConfiguration
from promo.models import PromoEmailConfiguration
from .forms import NewsletterForm
from bootstrap_modal_forms.generic import BSModalCreateView


class NewsletterView(BSModalCreateView):
    template_name = 'newsletter.html'
    form_class = NewsletterForm
    success_message = 'Dziękuję za zapis do newslettera'
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['newsletterConfiguration'] = MainConfiguration.objects.all()[:1].get()
        except MainConfiguration.DoesNotExist:
            context['newsletterConfiguration'] = MainConfiguration
        context['field_required_and_invalid'] = field_required_and_invalid
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        is_sent = self.send_email_to_customer(form)
        self.send_email_to_admin(form)
        self.show_status_message(is_sent)
        return super().post(self, request, *args, **kwargs)

    def show_status_message(self, is_sent):
        if is_sent:
            messages.add_message(self.request, messages.SUCCESS, 'Twoja wiadomość została wysłana.')
        else:
            messages.add_message(
                self.request,
                messages.ERROR,
                'Wysyłanie twojej wiadomości się nie powiodło. Skontaktuj się bezpośrednio pod adres: ' + self.get_email_configuration().from_email
            )

    def get_email_configuration(self):
        try:
            config = PromoEmailConfiguration.objects.all()
            email_configuration = config[:1].get()
        except PromoEmailConfiguration.DoesNotExist:
            email_configuration = PromoEmailConfiguration()
        return email_configuration

    def send_email_to_customer(self, form):
        recipient = form['email'].data
        if recipient:
            mail.send(
                [recipient],
                sender=self.get_email_configuration().from_email,
                template="potwierdzenie_newsletter",
                priority='now',
                context={
                    'imie': form['name'].data,
                    'email': form['email'].data,
                }
            )
            return True
        else:
            return False

    def send_email_to_admin(self, form):
        recipient = form['email'].data
        if recipient:
            mail.send(
                [self.get_email_configuration().admin_email],
                sender=self.get_email_configuration().from_email,
                template='potwierdzenie_newsletter_admin',
                priority='now',
                context={
                    'imie': form['name'].data,
                    'email': form['email'].data,
                }
            )

    def form_to_string(self, form):
        result = "{"
        for key, value in form.data.items():
            result += key + " : " + value + ", "
        result += "}"
        return result
