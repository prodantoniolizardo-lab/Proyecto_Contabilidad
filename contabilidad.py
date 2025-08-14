from dataclasses import dataclass
@dataclass
class la_tarea_de_los_gastos:
    descripcion: str
    monto_o_Valor: float
    fecha : str
gastos = la_tarea_de_los_gastos('dinero en compras de arboles', 500, '13/8/2025')
print (gastos)