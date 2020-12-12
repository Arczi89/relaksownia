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


def social_media_processor(request):
    # For _footer.html template file
    try:
        configuration = ContactConfiguration.objects.all()[:1].get()
        facebook = configuration.facebook
        twitter = configuration.twitter
        linkedin = configuration.linkedin
        instagram = configuration.instagram
        snapchat = configuration.snapchat
        youtube = configuration.youtube
        google_plus = configuration.google_plus
    except ContactConfiguration.DoesNotExist:
        facebook = None
        twitter = None
        linkedin = None
        instagram = None
        snapchat = None
        youtube = None
        google_plus = None
    return {
        'facebook': facebook,
        'twitter': twitter,
        'linkedin': linkedin,
        'instagram': instagram,
        'snapchat': snapchat,
        'youtube': youtube,
        'google_plus': google_plus
    }
