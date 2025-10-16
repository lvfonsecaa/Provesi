from ..models import Pedido, EstadoPedido

def get_pedido_estado(pk = int):
    pedido = Pedido.objects.get(pk=pk)
    return {
            "id": pedido.id,
            "estadoActual": pedido.estadoActual,
        }
