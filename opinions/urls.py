from django.urls import path

from . import views

urlpatterns = [
    path('', views.opinions, name='opinions'),
]
