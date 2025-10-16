from django.urls import path
from django.contrib import admin
from . import pedidos_view

urlpatterns = [
    path('pedidos/<int:pk>/estados/', pedidos_view.pedido_estado_view, name='pedidos-estados'),
]