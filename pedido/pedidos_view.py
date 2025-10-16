from django.http import JsonResponse
from django.core import serializers as serializer
from .logic import pedidos_logic as pl



def pedido_estado_view(request, pk:int):
    if request.method == 'GET':
        pedidos = pl.get_pedido_estado(pk)
        return JsonResponse(pedidos)