from django.utils.translation import ugettext_lazy as _

from .models import Newsletter
from bootstrap_modal_forms.forms import BSModalModelForm


class NewsletterForm(BSModalModelForm):
    class Meta:
        model = Newsletter
        labels = {
            'email': _('Adres e-mail'),
            'name': _('Imię'),
            'permission': _('Wyrażam zgodę na przesyłanie mi ofert marketingowych i promocyjnych drogą elektroniczną'),
        }
        fields = "__all__"
