proyecto = input("Escriba una breve descripcion del proyecto: ")
horas_estimadas = int(input("Escribas las horas estimadas para el proyecto: "))
valor_hora = int(input("¿Cual es el valor de la hora trabajda?: "))
tiempo_estimado = input("Escriba cuanto tiempo estima que tomara el proyecto: ")

print(proyecto)
print(horas_estimadas)
print(valor_hora)
print(tiempo_estimado)

valor_total = horas_estimadas * valor_hora

print(valor_total)

