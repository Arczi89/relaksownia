from django.urls import path

from . import views

urlpatterns = [
    path('', views.NewsletterView.as_view(), name='newsletter'),
]
