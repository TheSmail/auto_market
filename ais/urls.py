from django.urls import path

from .views import *

urlpatterns = [
    path('', orders_list, name='orders_list_url'),
    path('order/create/<int:pk>/', OrderCreateView.as_view(), name='create_order'),
    path('client/', clients_list, name='clients_list_url'),
    path('client/<int:pk>', ClientDetail.as_view(), name='client_detail_url'),



    path('contractors/', contractors_list, name='contractors_list_url'),
    # path('clients/', ClientListView.as_view()),
]
