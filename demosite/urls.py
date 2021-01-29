from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found, server_error, bad_request, permission_denied

urlpatterns = [
                  path('', include('main.urls')),
                  path('offer/', include('offer.urls')),
                  path('info/', include('info.urls')),
                  path('opinions/', include('opinions.urls')),
                  path('blog/', include('blog.urls')),
                  path('contact/', include('contact.urls')),
                  path('faq/', include('faq.urls')),
                  path('newsletter/', include('newsletter.urls')),
                  path('policy/', include('policy.urls')),
                  path('promo/', include('promo.urls')),
                  path('admin/', admin.site.urls),
                  path('djrichtextfield/', include('djrichtextfield.urls')),
                  path('400/', bad_request, kwargs={'exception': Exception('Bad Request!')}),
                  path('403/', permission_denied, kwargs={'exception': Exception('Permission Denied')}),
                  path('404/', page_not_found, kwargs={'exception': Exception('Page not Found')}),
                  path('500/', server_error),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

