from django.urls import path

from .views import *

urlpatterns = [
    path('clients/', ClientListView.as_view()),
]
