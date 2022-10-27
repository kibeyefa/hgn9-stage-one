from django.urls import path
from .views import *

urlpatterns = [
    path('', SlackDetailsView.as_view())
]
