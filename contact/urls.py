from django.urls import path

from . import views

urlpatterns = [
    # /contact
    path('', views.contact, name='contact')
]
