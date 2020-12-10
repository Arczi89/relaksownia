from contact.models import ContactConfiguration
from demosite.constants import default_contact_phone


def contact_phone_processor(request):
    # For _footer.html template file
    try:
        configuration = ContactConfiguration.objects.all()[:1].get()
        contact_phone = configuration.phone_number
    except ContactConfiguration.DoesNotExist:
        contact_phone = default_contact_phone
    return {
        'contact_phone': contact_phone
    }
