from django.urls import path

from . import views

urlpatterns = [
    # /contact
    path('', views.contact, name='contact'),
    # /contact/send_message
    path('send_message', views.contact_send_message, name='send_message')
]
