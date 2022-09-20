from django.urls import path
from .views import datasize, home, profile, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('datasize/', datasize, name='users-datasize'),
]
