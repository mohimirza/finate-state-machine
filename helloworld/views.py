from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from helloworld.models import Order
from helloworld.serializers import OrderSerializer


class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(["GET", "PATCH"])
def order_payment(self, product):
    obj = get_object_or_404(Order, product=product)
    obj.pay()
    obj.save()
    return Response("Changed state to paid")


@api_view(["GET", "PATCH"])
def order_fullfill(self, product):
    obj = get_object_or_404(Order, product=product)
    obj.fulfill()
    obj.save()
    return Response("Changed state to fullfill")


@api_view(["GET", "PATCH"])
def order_cancel(self, product):
    obj = get_object_or_404(Order, product=product)
    obj.cancel()
    obj.save()
    return Response("Changed state to cancelled")


@api_view(["GET", "PATCH"])
def order_return(self, product):
    obj = get_object_or_404(Order, product=product)
    obj._return()
    obj.save()
    return Response("Changed state to returned")
