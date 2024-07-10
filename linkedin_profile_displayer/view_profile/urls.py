from django.urls import path
from .views import view_profile, profile_input

urlpatterns = [
    path('', profile_input, name='profile_input'),
    path('<str:url>/', view_profile, name='profile_view'),
]