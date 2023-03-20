from django.urls import path

from helloworld.views import (
    OrderCreateView,
    OrderDetailView,
    order_cancel,
    order_fullfill,
    order_payment,
    order_return,
)

urlpatterns = [
    path("order/", OrderCreateView.as_view()),
    path("order/<int:pk>/", OrderDetailView.as_view()),
    path("payment/<str:product>/", order_payment),
    path("fulfill/<str:product>/", order_fullfill),
    path("cancel/<str:product>/", order_cancel),
    path("return/<str:product>/", order_return),
]
