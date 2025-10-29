import random
from datetime import datetime


def generar_ventas_aleatorias(carta, cantidad=120):

#Agrega ventas aleatorias mesa;fecha;hora;id_plato;cantidad

    try:
        arch = open("ventas.csv", "at", encoding="utf-8") #agregamos!!!

        platos = list(carta.keys())

        for i in range(cantidad):
            mesa = random.randint(1, 10)          # mesas del 1 al 10
            plato = random.choice(platos)         # id de plato
            hora = random.randint(19, 24)         # solo hora
            cantidad_platos = random.randint(1, 4)
            fecha = datetime.now().strftime("%Y-%m-%d")
            arch.write(f"{mesa};{fecha};{hora};{plato};{cantidad_platos}\n")

        arch.close()
        print(f"✅ Se agregaron {cantidad} ventas simuladas a 'ventas.csv' (sin borrar las reales)\n")

    except IOError:
        print(" Error al escribir el archivo")



def total_recaudado(carta):
#del dia
    total = 0
    hoy = datetime.now().strftime("%Y-%m-%d")
    try:
        arch = open("ventas.csv", "rt", encoding="utf-8")
        for linea in arch:
            mesa, fecha, hora, id_plato, cantidad = linea.strip().split(";")
            if fecha == hoy:  # solo ventas del día actual
                id_plato = str(id_plato)
                cantidad = int(cantidad)
                precio = carta[id_plato]["precio"]
                total += precio * cantidad
        arch.close()
        print(f"💰 Total recaudado del día ({hoy}): ${total:,.2f}\n")
    except IOError:
        print("No se pudo leer archivo ventas")


def mesa_que_mas_consumio(carta):
    consumo = {}
    hoy = datetime.now().strftime("%Y-%m-%d")
    try:
        arch = open("ventas.csv", "rt", encoding="utf-8")
        for linea in arch:
            mesa, fecha, hora, id_plato, cantidad = linea.strip().split(";")
            if fecha == hoy:  # solo del dia
                id_plato = str(id_plato)
                cantidad = int(cantidad)
                precio = carta[id_plato]["precio"]
                mesa = int(mesa)
                if mesa in consumo:
                    consumo[mesa] += precio * cantidad
                else:
                    consumo[mesa] = precio * cantidad
        arch.close()

        if consumo:
            mesa_top = max(consumo, key=consumo.get)
            print(f"🏆 Mesa que más consumió hoy ({hoy}): Mesa {mesa_top} (${consumo[mesa_top]:,.2f})\n")
        else:
            print("No hay ventas registradas para hoy.\n")

    except IOError:
        print("No se pudo leer ventas")


def generar_reporte_platos_top(carta):
#genera un archivo con los 10 platos más vendidos del día.

    hoy = datetime.now().strftime("%Y-%m-%d")
    conteo = {}   # id_plato: cantidad total vendida
    try:
        arch = open("ventas.csv", "rt", encoding="utf-8")

        for linea in arch:
            mesa, fecha, hora, id_plato, cantidad = linea.strip().split(";")
            if fecha == hoy:  # solo ventas del día
                id_plato = str(id_plato)
                cantidad = int(cantidad)
                if id_plato in conteo:
                    conteo[id_plato] += cantidad
                else:
                    conteo[id_plato] = cantidad
        arch.close()
        # Convertimos el diccionario en lista de tuplas
        lista_platos = [(id, cant) for id, cant in conteo.items()]
        # Ordenamos por cantidad (de mayor a menor) usando lambda
        lista_ordenada = sorted(lista_platos, key=lambda x: x[1], reverse=True)
        # Tomamos los 10 primeros
        top_10 = lista_ordenada[:10]
        # Guardamos el reporte CSV
        arch = open("platos_top.csv", "wt", encoding="utf-8")
        for id_plato, cantidad in top_10:
            nombre = carta[id_plato]["nombre"]
            arch.write(f"{nombre};{cantidad}\n")
        arch.close()
        print(f"🥇 Archivo 'platos_top.csv' generado con los 10 platos más vendidos del {hoy}")
    except IOError:
        print("Error al generar platos_top.csv")

def generar_reporte_ingredientes_masconsumidos(carta):
#10 ingredientes más consumidos del día

    hoy = datetime.now().strftime("%Y-%m-%d")
    consumo = {}  # ingrediente: cantidad total usada
    try:
        arch = open("ventas.csv", "rt", encoding="utf-8")
        for linea in arch:
            mesa, fecha, hora, id_plato, cantidad = linea.strip().split(";")
            if fecha == hoy:
                id_plato = str(id_plato)
                cantidad = int(cantidad)
                if id_plato in carta:
                    ingredientes = carta[id_plato]["ingredientes"]
                    for ingr, cant_por_plato in ingredientes.items():
                        total_usado = cant_por_plato * cantidad
                        if ingr in consumo:
                            consumo[ingr] = consumo[ingr] + total_usado
                        else:
                            consumo[ingr] = total_usado
        arch.close()
# por cantidad consumida (de mayor a menor)
        lista_ordenada = sorted(consumo.items(), key=lambda x: x[1], reverse=True)

        # me agarro los 10 de la lista
        top_10 = lista_ordenada[:10]
        try:
            arch2 = open("ingredientes_top.csv", "wt", encoding="utf-8")
            for ingr, cant in top_10:
                arch2.write(f"{ingr};{cant}\n")
            arch2.close()
            print(f"🥗 Archivo 'ingredientes_top.csv' generado con los 10 ingredientes más consumidos del {hoy}")
        except IOError:
            print("Error al escribir el archivo ingredientes_top.csv")

    except IOError:
        print("Error al leer el archivo ventas.csv")

def generar_reporte_ventas_horarias(carta):
#ventas totales por hora de 19 a 24
    hoy = datetime.now().strftime("%Y-%m-%d")
    ventas_por_hora = {hora: 0 for hora in range(19, 25)}  # 19,20,21,22,23,24
    try:
        arch = open("ventas.csv", "rt", encoding="utf-8")
        for linea in arch:
            mesa, fecha, hora, id_plato, cantidad = linea.strip().split(";")
            if fecha == hoy:
                hora = int(hora)
                cantidad = int(cantidad)
                id_plato = str(id_plato)
                if hora >= 19 and hora <= 24 and id_plato in carta:
                    precio = carta[id_plato]["precio"]
                    total = precio * cantidad
                    ventas_por_hora[hora] = ventas_por_hora[hora] + total
        arch.close()
        try:
            arch2 = open("ventas_horarias.csv", "wt", encoding="utf-8")
            for hora, total in ventas_por_hora.items():
                arch2.write(f"{hora};{total:.2f}\n")
            arch2.close()
            print(f"⏰ Archivo 'ventas_horarias.csv' generado con las ventas por hora del {hoy}")
        except IOError:
            print("Error al escribir el archivo ventas_horarias.csv")
    except IOError:
        print("Error al leer el archivo ventas.csv")