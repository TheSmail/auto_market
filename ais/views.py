from rest_framework.response import Response
from rest_framework.views import APIView

from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .utils import ObjectDetailMixin
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import *
from .serializers import ClientListSerializer

from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

class ClientListView(APIView):

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientListSerializer(clients, many=True)
        return Response(serializer.data)

# def order_create(request):
#     order = Order(request)
#     print(request.GET)
#     # client_id = int(request.POST['pk'])
#     client = get_object_or_404(Client, pk=client_id)
#     form = OrderCreateForm(request.POST)
#     if form.is_valid():
#         order.add(client=client)
#     return redirect('client_detail_url')


class OrderCreateView(View):
    # template_name = 'crud/create_order.html'
    # form_class = OrderForm
    # success_message = 'Отлично! Клиент создан'
    # success_url = reverse_lazy('clients_list_url')

    def get(self, request):
        return HttpResponse('Class based view')

    def post(self, request, pk):
        form = OrderForm(request.POST)
        client = Client.objects.get(id=pk)
        worker = User.objects.get(id=pk)
        if form.is_valid():
            form.client = client
            form.worker = worker
        form.save()
        return redirect(client.get_absolute_url())


def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders_list.html', context={'orders': orders})

class OrderDetail(ObjectDetailMixin, View):
    model = Order
    template = 'orders/order_detail.html'

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'orders/clients_list.html', context={'clients': clients})

class ClientDetail(ObjectDetailMixin, View):
    model = Client
    template = 'orders/client_detail.html'


def contractors_list(request):
    contractors = Contractor.objects.all()
    return render(request, 'orders/contractors_list.html', context={'contractors': contractors})