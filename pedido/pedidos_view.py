from django.http import JsonResponse
from django.core import serializers as serializer
from .logic import pedidos_logic as pl



def pedidos_view(request):
    if request.method == 'GET':
        pedidos = pl.get_pedidos()
        return JsonResponse(pedidos, safe=False)