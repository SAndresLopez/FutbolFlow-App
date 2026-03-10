from empleado import Empleado
from Empresa import Empresa

print("Sistema de Empleado")
empresa1=Empresa("IMK")
empresa1.contratar_empleado("Melissa", "contabilidad")
empresa1.contratar_empleado("Xiomara", "contabilidad")
empresa1.contratar_empleado("Andres", "Programador")
empresa1.contratar_empleado("López",  "Programador")

print(f"Total de empleados: {Empleado.obtener_total_empleados()}")

print(f"Empleados de contabilidad:"
      f"{empresa1.obtener_empleado_departamento("contabilidad")}")
empresa1.obtener_total_empleados() 