from django.urls import path
from .views import view_profile

urlpatterns = [
    path('<str:url>/', view_profile, name='profile_view'),
]