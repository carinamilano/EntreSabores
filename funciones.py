

# MÓDULO DE FUNCIONES - ENTRESABORES

from reportes import generar_ventas_aleatorias,total_recaudado,mesa_que_mas_consumio,generar_reporte_platos_top,generar_reporte_ingredientes_masconsumidos,generar_reporte_ventas_horarias,generar_reporte_tipos_platos
from datetime import datetime
import json
import random
# -------------------- LOG IN -----------------------#

def log_in():
    while True:
        usuario = input("Ingrese usuario: ")
        contrasena = input("Ingrese contraseña: ")
        encontrado = False
        try:
            arch = open("usuarios.txt", "rt",encoding="utf-8")
        except IOError:
            print("Error! No se pudo abrir el archivo de usuarios")
        else:
            for linea in arch:
                datos = linea.strip().split(";")
                if usuario == datos[0] and contrasena == datos[1]:
                    encontrado = True
                    break
            arch.close()
        if encontrado:
            print("Sesión iniciada con éxito! Bienvenido", usuario)
            break
        else:
            print("Usuario y/o contraseña no válidos")
    return usuario

# -------------- GENERACIÓN ARCHIVOS USUARIOS.TXT -----------------------#
def generar_archivo_usuarios():
    dic_usuario = {
        "admin": "123",
        "mozo1": "abc"
    }
    try:
        archUsuarios = open("usuarios.txt", "wt")
    except IOError:
        print("No se pudo crear archivo")
    else:
        for usuario in dic_usuario:
            archUsuarios.write(f"{usuario};{dic_usuario[usuario]}\n")
        archUsuarios.close()

# -------------- GENERACIÓN ARCHIVOS STOCK.CSV-----------------------#
def cargar_stock():
    stock = {}
    try:
        arch = open("stock.csv", "rt", encoding="utf-8")
        for linea in arch:
            ingrediente,cantidad = linea.strip().split(";")
            stock[ingrediente] = int(cantidad)
        arch.close()
    except IOError:
        print(" No se encontró stock.csv. Se cargara stock basico......")
        stock = {
            "carne": 15,
            "papas": 25,
            "harina": 20,
            "queso": 18,
            "tomate": 15,
            "cebolla": 10,
            "quinoa": 12,
            "zanahoria": 10,
            "brocoli": 8,
            "pollo": 12,
            "arroz": 15,
            "lechuga": 10,
            "atun": 8,
            "aceitunas": 6,
            "huevo": 12,
            "jamon": 10,
            "pan": 20,
            "palta": 8,
            "panceta": 10,
            "crema":15,
            "pan rallado":10,
            "brócoli": 10,
            "soja": 12,
            "calabaza":10,
            "masa":11,
            "croutons":8,
            "lentejas":15,
            "ajo":20,
            "hongos":12,
            "curry": 10,
            "maíz": 11,
            "porotos":15
        }
        guardar_stock(stock)
    return stock

def guardar_stock(stock):
    try:
        arch = open("stock.csv", "wt", encoding="utf-8")
        for ingr, cant in stock.items():
            arch.write(f"{ingr};{cant}\n")
        arch.close()
        print("Archivo stock.csv guardado correctamente.")
    except IOError:
        print("Error al guardar el archivo de stock.")


# -------------- REGISTROS DEL LOG -----------------------#

def registrar_evento(opcion, archivo="registros_eventos.txt"):
    try:
        marca = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arch = open(archivo, "at",encoding="utf-8")
        arch.write(marca + ";" + opcion + ";" + "\n")
        arch.close()
    except IOError:
        print("No se pudo crear registro de logs")





# -------------- GESTIÓN DEL ARCHIVO JSON ----------------------#

def cargar_carta():
#Carga la carta desde carta.json. Si no existe, crea una carta base con 10 platos iniciales
    try:
        arch = open("carta.json", "rt", encoding="utf-8")
        carta = json.load(arch)
        arch.close()
    except FileNotFoundError:
        print("No se encontró carta.json. Creando archivo con una carta base...")
        carta = {
            1: {
                "nombre": "Milanesa con papas",
                "precio": 35500.00,
                "ingredientes": {
                    "carne": 1,
                    "huevo": 1,
                    "pan rallado": 1,
                    "papas": 2
                },
                "tipo": "carnívoro"
            },
            2: {
                "nombre": "Pizza muzzarella",
                "precio": 39500.50,
                "ingredientes": {
                    "harina": 1,
                    "queso": 1,
                    "tomate": 1
                },
                "tipo": "vegetariano"
            },
            3: {
                "nombre": "Bowl de quinoa",
                "precio": 41500.00,
                "ingredientes": {
                    "quinoa": 1,
                    "zanahoria": 1,
                    "brócoli": 1
                },
                "tipo": "vegano"
            },
            4: {
                "nombre": "Hamburguesa veggie",
                "precio": 38500.75,
                "ingredientes": {
                    "soja": 1,
                    "pan": 1,
                    "lechuga": 1,
                    "tomate": 1
                },
                "tipo": "vegetariano"
            },
            5: {
                "nombre": "Tarta de calabaza",
                "precio": 36500.00,
                "ingredientes": {
                    "calabaza": 1,
                    "huevo": 1,
                    "masa": 1,
                    "queso": 1
                },
                "tipo": "vegetariano"
            },
            6: {
                "nombre": "Ensalada César",
                "precio": 35200.00,
                "ingredientes": {
                    "pollo": 1,
                    "lechuga": 1,
                    "queso": 1,
                    "croutons": 1
                },
                "tipo": "carnívoro"
            },
            7: {
                "nombre": "Sopa de lentejas",
                "precio": 37200.50,
                "ingredientes": {
                    "lentejas": 1,
                    "zanahoria": 1,
                    "cebolla": 1,
                    "ajo": 1
                },
                "tipo": "vegano"
            },
            8: {
                "nombre": "Risotto de hongos",
                "precio": 46500.00,
                "ingredientes": {
                    "arroz": 1,
                    "hongos": 1,
                    "crema": 1,
                    "queso": 1
                },
                "tipo": "vegetariano"
            },
            9: {
                "nombre": "Pollo al curry",
                "precio": 52500.00,
                "ingredientes": {
                    "pollo": 1,
                    "curry": 1,
                    "arroz": 1,
                    "crema": 1
                },
                "tipo": "carnívoro"
            },
            10: {
                "nombre": "Tacos de maíz",
                "precio": 39800.00,
                "ingredientes": {
                    "maíz": 1,
                    "palta": 1,
                    "porotos": 1,
                    "cebolla": 1
                },
                "tipo": "celíaco"
            }
        }
        guardar_carta(carta)
    return carta

def guardar_carta(carta):
#Guarda el menú actualizado en el archivo JSON
    try:
        arch = open("carta.json", "wt", encoding="utf-8")
        json.dump(carta, arch, indent=4, ensure_ascii=False) #dump="vuelca,graba", ensure_ascii=False: No conviertas los caracteres acentuados a códigos Unicode, dejalos tal cual
        arch.close()
        print("Carta guardada correctamente.")
    except IOError:
        print("Error al guardar la carta.")

# -------------- FUNCIONES GENÉRICAS -----------------------#

#funcion GENERICA para validar un ingreso de un num entero dentro de un rango
def numeroEntreRango(num1, num2, texto):
    while True:
        try:
            num = int(input(texto))
            if num < num1 or num > num2:
                raise ValueError
            break
        except ValueError:
            print("Error, debe ingresar opción válida")
    return num

# función GENERICA para ingresar un único número
def ingresar_num_entero(num,texto):
    while True:
        try:
            n = int (input (texto))
            if n != num:
                raise ValueError
            break
        except ValueError:
            print ("Error! Opción no válida")
    return n

# funcion GENERICA para ingresar un numero mayor a N
def ingresar_num_mayor_a(num_base,texto):
    while True:
        try:
            num = int(input(texto))
            if num < num_base:
                raise ValueError
            break
        except ValueError:
            print("Error, valor ingresado inválido")
    return num

# función GENERICA para ingresar un valor float positivo
def ingresar_valor_float_positivo(texto):
    while True:
        try:
            num = float(input(texto))
            if num < 1:
                raise ValueError
            break
        except ValueError:
            print("Error, valor ingresado inválido")
    return num

# función GENERICA para ingresar un string no númerico mayor a N caracteres
def str_minimo_n_caracteres (n,texto):
    while True:
        try:
            info = input(texto).strip()
            if info.isdigit() or  len(info)<=n:
                raise ValueError
            break
        except ValueError:
            print (f"Error! El dato ingresado debe ser mayor a {n} caracteres y no puede ser númerico")
    return info

# -------------- M1: TOMAR PEDIDO -----------------------#

def tomar_pedido(carta, stock, pedidos):
    """
    Toma pedidos por mesa:
    - Usa `temp_stock` para descontar stock temporalmente mientras la mesa agrega ítems.
    - Si la mesa confirma, se persiste temp_stock a stock.csv (usando guardar_stock).
    - Si la mesa cancela, no se modifica el archivo ni el diccionario stock original.
    """

    while True:
        num_mesa = numeroEntreRango(0, 10, "Ingrese el número de mesa(1-10). 0 para volver al menú: ")
        if num_mesa == 0:
            break

        # Inicializo pedidos para la mesa si no existe (pero no confirmo aún)
        if num_mesa not in pedidos:
            pedidos[num_mesa] = {}

        # temp_stock = copia del stock real; se modifica durante la sesión de la mesa
        temp_stock = {k.lower(): int(v) for k, v in stock.items()}

        # carrito es lo que esta mesa está pidiendo en ESTA sesión (no persistido hasta confirmar)
        carrito = {}  # id_plato (str) -> cantidad pedida en esta sesión

        mostrar_carta_id()

        while True:
            id_plato = input("Ingrese el id del plato (Vacío para terminar): ").strip()
            if id_plato == "":
                break

            try:
                if not id_plato in carta:  
                    raise ValueError
                
            except ValueError:
                print("Plato inexistente, intente de nuevo")
                continue
            nombre_plato = carta[id_plato]['nombre']
                
            cantidad = ingresar_num_mayor_a(1, f"Ingrese la cantidad de '{nombre_plato}': ")

            # Verificar stock suficiente usando temp_stock (reserva temporal)
            ingredientes_necesarios = carta[id_plato]["ingredientes"]

            falta = []
            for ingr, cant_por_unidad in ingredientes_necesarios.items():
                ingr_key = ingr.lower()
                if ingr_key not in temp_stock:
                    falta.append(ingr)
                else:
                    # cantidad total requerida para este item
                    requerido = cant_por_unidad * cantidad
                    if temp_stock[ingr_key] < requerido:
                        falta.append(ingr)

            if falta:
                print(f"No hay stock suficiente de: {', '.join(falta)}")
                print("Revisá cantidades o elegí otro plato/ingrediente.")
                continue

            # Si pasa la verificación: descontar de temp_stock (reserva temporal)
            for ingr, cant_por_unidad in ingredientes_necesarios.items():
                ingr_key = ingr.lower()
                temp_stock[ingr_key] -= cant_por_unidad * cantidad

            # Agregar al carrito (acumula si se agrega el mismo plato varias veces)
            id_key = str(id_plato)  # uso str para normalizar en carrito/pedidos
            if id_key in carrito:
                carrito[id_key] += cantidad
            else:
                carrito[id_key] = cantidad

            print(f"Pedido agregado al carrito: {nombre_plato} x {cantidad}")
            # Mostrar stock temporal (opcional, útil para debugging)
            # print("Stock temporal (después de reservar):", temp_stock)

        # Al terminar de agregar platos para la mesa, muestro resumen del carrito
        if carrito:
            print(f"\nResumen de la mesa {num_mesa}:")
            total = 0
            for id_k, cant in carrito.items():
                # como carta puede tener claves int o str, busco la entrada correcta
                key = id_k if id_k in carta else int(id_k)
                nombre = carta[key]["nombre"]
                precio = carta[key]["precio"]
                subtotal = precio * cant
                total += subtotal
                print(f"- {nombre} x {cant} → ${subtotal: }")
            print(f"Total a pagar: ${total: }")

            # Pregunto si confirma o cancela
            confirmar = input("Confirmar pedido y actualizar stock? (S/N): ").strip().lower()
            if confirmar == 's' or confirmar == 'si':
                # Persistir temp_stock a archivo y actualizar el diccionario stock en memoria
                #try:
                    # Uso tu función guardar_stock si existe

                guardar_stock({k: v for k, v in temp_stock.items()})

                # Actualizo el diccionario stock pasado por parámetro para que el resto del programa
                # trabaje con los valores actualizados en memoria
                stock.clear()
                for k, v in temp_stock.items():
                    stock[k] = v

                # Finalmente, vuelco el carrito a pedidos (acumulo si ya había pedidos previos)
                if num_mesa not in pedidos:
                    pedidos[num_mesa] = {}
                for id_k, cant in carrito.items():
                    if id_k in pedidos[num_mesa]:
                        pedidos[num_mesa][id_k] += cant
                    else:
                        pedidos[num_mesa][id_k] = cant

                print("Pedido confirmado y stock actualizado.")
            else:
                # Si cancela, no se hace nada con stock ni con pedidos
                print("Pedido cancelado. No se modificó el stock ni se guardó el pedido.")
        else:
            print("No se agregaron platos para esta mesa.")

    return pedidos


# -------------- M2: CERRAR MESA -----------------------#
def cerrar_mesa(carta,stock,pedidos):
    if pedidos:
        suma_mesa = 0
        cantidad_platos = 0

        print     ("---------MESAS ACTIVAS---------")
        for num_mesa in pedidos:
            print (f"MESA N° {num_mesa}")
            print ("Pedido: ")
            for id_plato in pedidos[num_mesa]:
                print(f"ID: {id_plato} | {carta[id_plato]['nombre']} | Cantidad: {pedidos[num_mesa][id_plato]} | ${carta[id_plato]['precio']*pedidos[num_mesa][id_plato]}")
                suma_mesa += carta[id_plato]['precio'] * pedidos[num_mesa][id_plato]
                cantidad_platos += pedidos[num_mesa][id_plato]
            print (f"Total Mesa N°{num_mesa}: ${suma_mesa}")
            print ("-------------------------------")

        while True:
            try: 
                mesa_a_cerrar = numeroEntreRango (0,10,"Ingrese la mesa que desea cerrar (0 para volver al menú): ")
                if mesa_a_cerrar == 0:
                    break

                if mesa_a_cerrar not in pedidos:
                    raise ValueError ("Mesa inactiva, reintente con otra mesa.")
                break
            except ValueError as msg:
                print (msg)
        
        if mesa_a_cerrar != 0:
            try:
                arch = open("ventas.csv", "at", encoding="utf-8") 

                plato = list(carta.keys())
                
                
                for id_plato in pedidos[mesa_a_cerrar]:
                    mesa = mesa_a_cerrar          # mesas del 1 al 10
                    plato = id_plato   # id de plato
                    cantidad_platos = pedidos[num_mesa][id_plato] 
                    fecha = datetime.now().strftime("%Y-%m-%d")
                    hora = datetime.now().strftime('%H:%M:%S')       # solo hora
                    arch.write(f"{mesa};{fecha};{hora};{plato};{cantidad_platos}\n")

                arch.close()
                del pedidos[mesa_a_cerrar]
                print(f"Se registró la venta de la mesa N° {num_mesa}")
                print (f"Mesa N° {num_mesa} liberada")
                cerrar_mesa(carta,stock,pedidos)

            except IOError:
                print(" Error al escribir el archivo")


    else: 
        print ("No hay ninguna mesa activa")

        volver = ingresar_num_entero(0, "Ingrese 0 para volver al menú: ")
        if volver == 0:
            menu_principal(carta, stock,pedidos)


# -------------- MOSTRAR CARTA (normal) -----------------------#
# reemplazamos esta funcion por la de mostrar_carta_id() ya que implementamos recursividad


def mostrar_carta(carta,stock,pedidos): #muestra los platos de la carta con sus ingredientes y precio
    try:
        arch=open("carta.json","rt", encoding="utf-8")
        carta=json.load(arch)
        arch.close()
        print("\n📜 ----- CARTA DE PLATOS ----- 📜")
        for id, datos in carta.items():
            print(f"\n🍽️  ID:{id} {datos['nombre']}")
            print(f"   💲 Precio: ${datos['precio']:.2f}")
            print(f"   🏷️ Tipo: {datos['tipo']}")
            print(f"   🧂 Ingredientes:{datos['ingredientes']}")
        print("\n")
    except IOError:
        print("Error con los archivos")

#---------------- M3: MOSTRAR CARTA EN ORDEN -----------------------#
# Mostrar carta por ID (ascendente)
def mostrar_carta_id (carta=None, ids=None, indice=0):
    if carta is None:
        try:
            arch=open("carta.json","rt", encoding="utf-8")
            carta=json.load(arch)
            arch.close()
        except IOError:
            print ("Error al abrir archivo")

    while True:
        #Si no se pasaron los IDs, los obtenemos y los ordenamos
        if ids is None: 
            ids = sorted(carta.keys(), key = lambda x: int(x)) # ordenar por número ascendente
            print("\n📜 CARTA (ordenada por ID ascendente)\n" + "-" * 45)
            #print (ids)

        # caso base: si ya mostramos todos los platos, terminamos
        if indice == len(ids):
            print("\nFin de la carta.\n")
            break
        
        # mostramos el plato actual
        id_actual = ids[indice]
        datos = carta[id_actual]
        print(f"\n🍽️  ID:{id_actual} {datos['nombre']}")
        print(f"   💲 Precio: ${datos['precio']:.2f}")
        print(f"   🏷️ Tipo: {datos['tipo']}")
        print(f"   🧂 Ingredientes: {', '.join(datos['ingredientes'].keys())}")

        # llamada recursiva para mostrar el siguiente plato
        mostrar_carta_id(carta, ids, indice + 1)
        break
# ------------- M4: MOSTRAR STOCK --------------#

def mostrar_stock(carta,stock,pedidos):
    try:
        print("\n📦 STOCK DE INGREDIENTES 📦")
        for ingrediente, cantidad in stock.items():
            print(f"{ingrediente:<12}{cantidad:>3}")
        print()
        volver = ingresar_num_entero(0, "Ingrese 0 para volver al menú: ")
        if volver == 0:
            menu_principal(carta, stock,pedidos)
    except IOError:
        print("Error con archivo")

# -------------M5: SUBMENÚ MODIFICAR CARTA--------------#
def submenu_modificar_carta(carta,stock,pedidos):
    print("----MODIFICAR CARTA----")
    print ("1. Agregar plato")
    print ("2. Eliminar plato")
    print ("3. Modificar plato")
    print ("0. Salir")

    opcion = numeroEntreRango (0,3,"Ingrese una opción: ")
    if opcion == 0:
        registrar_evento ("Menú principal")
        menu_principal(carta, stock,pedidos)
    elif opcion == 1:
        registrar_evento ("Agregar plato")
        nueva_entrada = agregar_plato(carta)
        menu_principal(carta,stock,pedidos)
    elif opcion == 2:
        registrar_evento("Eliminar plato")
        carta = eliminar_plato(carta,pedidos)
        menu_principal(carta,stock,pedidos)
    elif opcion == 3:
        registrar_evento("Modificar plato")
        modificar_plato(carta)
        menu_principal(carta, stock, pedidos)

# -------------- SUB1: AGREGAR PLATO -----------------------#

def agregar_plato(carta):
    try:
        arch = open ("stock.csv", "rt", encoding="utf-8")
    except IOError:
        print ("Error al cargar archivos")
    else:
        dic_ingredientes = {}
        stock_nombres = []
        for linea in arch:
            nombre, cantidad = linea.strip().split(";")
            stock_nombres.append (nombre)
        
        while True:
            try:
                print("ID de platos ya utilizados:", ",".join(carta.keys()))
                id_plato = str(ingresar_num_mayor_a(1,"Ingrese ID del plato: "))
                if id_plato in carta:
                    raise ValueError
                
                break
            except ValueError:
                print ("Error, ID de plato ya existente!")

        plato_a_agregar = str_minimo_n_caracteres(3,"Ingrese el nombre del plato a agregar: ")

        precio = ingresar_valor_float_positivo(f"Ingrese el precio de {plato_a_agregar}: $")

        print("\n🧂 Ingredientes disponibles en stock:\n")
        for i in range(0, len(stock_nombres), 10):  # Muestra 10 ingredientes por línea
            print(", ".join(stock_nombres[i:i + 10]))
        print("-" * 70)

        while True:
            try: 
                ingredientes = input (f"Ingrese los ingredientes que tiene {plato_a_agregar}. Vacío para dejar de cargar ingredientes: ").strip().lower()
                
                if ingredientes == "" and dic_ingredientes:
                    break
                elif not dic_ingredientes and ingredientes == "":
                    print ("No se puede cargar un plato sin ingredientes.")
                    continue

                if ingredientes not in stock_nombres:
                    raise ValueError
                        
                cantidad_ingredientes = ingresar_num_mayor_a(1,f"Ingrese la cantidad de {ingredientes} que lleva {plato_a_agregar}: ")

                dic_ingredientes[ingredientes] = cantidad_ingredientes
            
            except ValueError:
                print ("Ingrediente ingresado no válido")
                continue
        
        tipo = numeroEntreRango (1,4,"Ingrese el tipo de plato: 1. Carnivoro | 2. Vegetariano | 3. Vegano | 4. Celíaco: ")
        if tipo == 1:
            plato_tipo = "carnivoro"
        elif tipo == 2:
            plato_tipo = "vegetariano"
        elif tipo == 3:
            plato_tipo = "vegano"
        elif tipo == 4:
            plato_tipo = "celíaco"

        nueva_entrada = {id_plato: {
        "nombre": plato_a_agregar.title(),
        "precio": float(precio),
        "ingredientes": dic_ingredientes,
        "tipo": plato_tipo }}
        arch.close()

        try:
            arch1 = open("carta.json", "rt", encoding="utf-8")
            datos = json.load(arch1)
            datos.update(nueva_entrada)

            arch2 = open ("carta.json","wt",encoding="utf-8")
            json.dump(datos, arch2, indent=4, ensure_ascii=False)

            arch1.close()
            arch2.close()
            carta.update(nueva_entrada)

            print("Plato nuevo agregado correctamente a la carta.")
            
        except IOError:
            print("Error al guardar la carta.")


# -------------- SUB2: ELIMINAR PLATO -----------------------#

def eliminar_plato(carta,pedidos):
    print(" 🍽️  Platos actuales en la carta:")
    for id_plato, datos in carta.items():
        print(f"{id_plato}. {datos['nombre']}")

    while True:
        try:
            id_a_eliminar = input("Ingrese el número del plato que desea eliminar: ")

            if id_a_eliminar.strip() == "":
                raise ValueError("Debe ingresar un número de plato.")
            if id_a_eliminar not in carta:
                raise ValueError("No existe ese plato en la carta.")
            

            for info in pedidos:
                if id_a_eliminar in pedidos[info]:
                    raise ValueError ("No se puede eliminar un plato ya pedido!")


            del carta[id_a_eliminar]

            try:
                arch = open("carta.json", "w", encoding="utf-8")
                json.dump(carta, arch, ensure_ascii=False, indent=4)
                arch.close()
            except IOError:
                print(f"Error al guardar los cambios en carta")
                break

            print(f"Plato {id_plato}. {datos['nombre']} eliminado correctamente.")
            break

        except ValueError as msg:
            print(msg)
    return carta

# -------------- SUB3: MODIFICAR PLATO -------------------------------------------------------------------#
def modificar_plato(carta):
    try:
        print("🍽️  PLATOS DISPONIBLES EN LA CARTA:")
        for id_plato, datos in carta.items():
            print(f"{id_plato}. {datos['nombre']} - ${datos['precio']} ({datos['tipo']})")
        print("-" * 60)

        id_a_modificar = str(numeroEntreRango(1, len(carta), "Ingrese el número del plato que desea modificar: "))
        if id_a_modificar not in carta:
            raise ValueError(" No existe un plato con ese número en la carta.")

        plato = carta[id_a_modificar]
        print(f"\n✏️ MODIFICANDO: {plato['nombre']}")
        print("Presione Enter para mantener el valor actual.\n")

        nuevo_nombre = input("Ingrese el nuevo nombre del plato (Enter para mantener): ").strip()
        if nuevo_nombre != "":
            if len(nuevo_nombre) < 4 or nuevo_nombre.isnumeric():
                print("El nombre debe tener al menos 4 caracteres y no ser numérico. Se mantiene el actual.")
            else:
                plato["nombre"] = nuevo_nombre.title()

        nuevo_precio = input("Ingrese el nuevo precio (Enter para mantener): ").strip()
        if nuevo_precio != "":
            try:
                valor = float(nuevo_precio)
                if valor <= 0:
                    raise ValueError
                plato["precio"] = valor
            except ValueError:
                print(" El precio debe ser numérico y mayor que cero. Se mantiene el actual.")

        nuevo_tipo = input("Ingrese el nuevo tipo (carnivoro, vegetariano, vegano, celiaco) o Enter para mantener: ").lower().strip()
        if nuevo_tipo != "":
            if nuevo_tipo in ["carnivoro", "vegetariano", "vegano", "celiaco"]:
                plato["tipo"] = nuevo_tipo
            else:
                print("Tipo inválido. Se mantiene el actual.")

        stock_disponible = []
        try:
            arch_stock = open("stock.csv", "rt", encoding="utf-8")
            for linea in arch_stock:
                nombre, cantidad = linea.strip().split(";")
                stock_disponible.append(nombre)
            arch_stock.close()
        except IOError:
            print("No se pudo abrir stock.csv.")

        print("\n🧂 LISTA DE INGREDIENTES DISPONIBLES:")
        for i, ing in enumerate(stock_disponible, start=1):
            print(f"{i} - {ing}")
        print("-" * 50)
        print("Ingrese el número del ingrediente a agregar y luego la cantidad.")
        print("Cuando haya terminado, ingrese 0 para finalizar.\n")

        nuevos_ingredientes = {}
        while True:
            try:
                num_ing = numeroEntreRango(0, len(stock_disponible),"Ingrediente N° (0 para terminar): ")
                if num_ing == 0:
                    break
                ingrediente_elegido = stock_disponible[num_ing - 1]
                cantidad = ingresar_num_mayor_a(0, f"Ingrese la cantidad de '{ingrediente_elegido}': ")
                nuevos_ingredientes[ingrediente_elegido] = cantidad
            except ValueError as msg:
                print(msg)
        if nuevos_ingredientes:
            plato["ingredientes"] = nuevos_ingredientes
        else:
            print("No se seleccionaron ingredientes nuevos. Se mantienen los actuales.")
        carta[id_a_modificar] = plato
        try:
            arch = open("carta.json", "w", encoding="utf-8")
            json.dump(carta, arch, ensure_ascii=False, indent=4)
            arch.close()
            print(f"\nPlato '{plato['nombre']}' modificado correctamente.")
        except IOError:
            print("Error al guardar los cambios en carta.json.")

    except ValueError as msg:
        print(f"Error en ingreso de datos: {msg}")


# -------------- MENÚ PRINCIPAL---------------------------------------------------------#
def menu_principal(carta, stock,pedidos):
    print("\n🍷 ----- Menú EntreSabores ----- 🍷")
    print(" 1️⃣  🧾 Tomar pedido")
    print(" 2️⃣  💵 Cerrar mesa")
    print(" 3️⃣  📜 Mostrar carta (orden por)")
    print(" 4️⃣  📦 Mostrar stock de ingredientes")
    print(" 5️⃣  ✏️ Modificar carta")
    print(" 6️⃣  📊 Ver reportes")
    print(" 0️⃣  🚪 Salir")
    print()
    opcion = numeroEntreRango(0, 6, "Ingrese una opción: ")
    print()
    if opcion == 1:
        registrar_evento("Tomar pedido")
        pedido = tomar_pedido(carta, stock,pedidos)
        menu_principal(carta, stock,pedidos)
    elif opcion == 2:
        registrar_evento("Cerrar mesa")
        cerrar_mesa(carta, stock,pedidos)
        menu_principal(carta, stock,pedidos)
    elif opcion == 3:
        registrar_evento("Mostrar carta")
        #mostrar_carta(carta,stock,pedidos)
        mostrar_carta_id()
        volver = ingresar_num_entero(0,"Ingrese 0 para volver al menú: ")
        if volver == 0:
            menu_principal(carta, stock,pedidos)
    elif opcion == 4:
        registrar_evento("Mostrar stock de ingredientes")
        mostrar_stock(carta,stock,pedidos)
    elif opcion == 5:
        registrar_evento("Modificar carta")
        submenu_modificar_carta(carta,stock,pedidos)
    elif opcion == 6:
        registrar_evento("Ver reportes")
        generar_ventas_aleatorias(carta)  # genera ventas simuladas
        total_recaudado(carta)  # muestra el total
        mesa_que_mas_consumio(carta)  # muestra la mesa top
        generar_reporte_platos_top(carta)
        generar_reporte_ingredientes_masconsumidos(carta)
        generar_reporte_ventas_horarias(carta)
        generar_reporte_tipos_platos(carta)
        volver = ingresar_num_entero(0,"Ingrese 0 para volver al menú: ")
        if volver == 0:
            menu_principal(carta, stock,pedidos)







