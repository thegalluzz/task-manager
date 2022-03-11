from django.urls import path, include
from .views import *

urlpatterns = [
    path("contact-form/",
         ContactFormAPI.as_view(), name="contact-form"),
    path("auth/", include('rest_auth.urls')),
    path("auth/registration/", include('rest_auth.registration.urls')),
]
