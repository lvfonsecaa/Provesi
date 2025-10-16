from django.urls import path
from django.contrib import admin
from . import pedidos_view

urlpatterns = [
    path('pedidos/estados/', pedidos_view.pedidos_view, name='pedidos-estados'),
]