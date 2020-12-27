from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('main.urls')),
                  path('offer/', include('offer.urls')),
                  path('info/', include('info.urls')),
                  path('opinions/', include('opinions.urls')),
                  path('blog/', include('blog.urls')),
                  path('contact/', include('contact.urls')),
                  path('faq/', include('faq.urls')),
                  path('newsletter/', include('newsletter.urls')),
                  path('admin/', admin.site.urls),
                  path('djrichtextfield/', include('djrichtextfield.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

