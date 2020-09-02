from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('delivery.html', views.delivery, name="delivery"),
    path('contact.html', views.contact, name="contact"),
    path('faq.html', views.faq, name="faq"),
    ]