from ..models import Pedido, EstadoPedido

def get_pedidos():
    pedidos = Pedido.objects.all()
    return [
        {
            "id": p.id,
            "estadoActual": p.estadoActual,
        }
        for p in pedidos
    ]
