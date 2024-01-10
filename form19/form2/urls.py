# signup/urls.py
from django.urls import path
from .views import signup_view

urlpatterns = [
    path('signup/', signup_view, name='signup_view'),
    # Add more paths as needed
]