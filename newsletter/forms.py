from .models import Newsletter
from bootstrap_modal_forms.forms import BSModalModelForm


class NewsletterForm(BSModalModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
