

# MÓDULO DE FUNCIONES - ENTRESABORES

from datetime import datetime
import json

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
            ingrediente, cantidad = linea.strip().split(";")
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
            continue
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
            continue
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
            continue
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
            continue
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
    while True:
        num_mesa = numeroEntreRango (0,10,"Ingrese el número de mesa(1-10). 0 para volver al menú: ")
        if num_mesa == 0:
            break

        if num_mesa not in pedidos:
            pedidos[num_mesa] = {}  # crear nueva entrada para la mesa

        carrito = {}  # plato -> cantidad pedida en esta sesión

        mostrar_carta(carta,stock,pedidos)
        opciones = len (carta)
        
        while True:
            id_plato = numeroEntreRango (0,10,"Ingrese el id del plato (0 para terminar): ")
            if id_plato == 0:
                break
            
            id_plato = str (id_plato)
            nombre_plato = carta[id_plato]['nombre']
            
            if str(id_plato) not in carta:
                print("Plato inexistente, intente de nuevo")
                continue

            cantidad = ingresar_num_mayor_a(1,f"Ingrese la cantidad de '{nombre_plato}': ")

            # cargar stock desde CSV
            stock_dict = {}
            try:
                arch_stock = open("stock.csv", "rt", encoding="utf-8")
            except IOError:
                print("No se pudo abrir stock.csv")
            else:
                for linea in arch_stock:
                    nombre,cantidad_stock = linea.strip().split(";")
                    stock_dict[nombre] = cantidad_stock
                arch_stock.close()

            # verificar stock suficiente
            ingredientes_necesarios = carta[id_plato]["ingredientes"]

            falta = []
            for ingr, cant in ingredientes_necesarios.items():
                stock_ingrediente = int(stock_dict[ingr.lower()])
                if ingr.lower() not in stock_dict:
                    falta.append(ingr)
                elif stock_ingrediente < cant * cantidad:
                    falta.append(ingr)

            if falta:
                print(f"No hay stock suficiente de: {', '.join(falta)}")
                continue

            # descontar stock
            for ingr, cant in ingredientes_necesarios.items():
                stock_ingrediente = int(stock_dict[ingr.lower()])
                stock_ingrediente -= cant * cantidad

            # actualizar CSV
            try:
                arch_stock = open("stock.csv", "wt", encoding="utf-8")
            except IOError:
                print("No se pudo actualizar stock.csv")
            else:
                arch_stock.write("ingrediente;cantidad\n")
                for ingr, cant in stock_dict.items():
                    arch_stock.write(f"{ingr};{cant}\n")
                arch_stock.close()

            # actualizar pedidos
            if id_plato in pedidos[num_mesa]:
                pedidos[num_mesa][id_plato] += cantidad
            else:
                pedidos[num_mesa][id_plato] = cantidad

            print(f"Pedido agregado: {nombre_plato} x {cantidad}")

        # mostrar resumen mesa
        if pedidos[num_mesa] and id_plato != "0":
            print(f"\n Pedido mesa {num_mesa}:")
            total = 0
            for id_plato, cant in pedidos[num_mesa].items():
                precio = carta[id_plato]["precio"] * cant
                total += precio
                print(f"- {nombre_plato} x {cant} → ${precio}")
            print(f"Total a pagar: ${total}")

    return pedidos


# -------------- M3: MOSTRAR CARTA -----------------------#

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

# ------------- M4: MOSTRAR STOCK --------------#
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
        guardar_agregar_plato (nueva_entrada)
        menu_principal(carta, stock,pedidos)
    elif opcion == 2:
        registrar_evento ("Eliminar plato")
        #eliminar_plato()
    elif opcion == 3:
        registrar_evento ("Modificar plato")
        #modificar_plato()
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
        guardar_agregar_plato (nueva_entrada)
        menu_principal(carta, stock,pedidos)
    elif opcion == 2:
        registrar_evento ("Eliminar plato")
        #eliminar_plato()
    elif opcion == 3:
        registrar_evento ("Modificar plato")
        #modificar_plato()

# -------------- SUB1: AGREGAR PLATO -----------------------#

def agregar_plato(carta):
    try:
        archLec = open ("stock.csv","rt")
    except IOError:
        print ("Error al cargar archivos")
    else:
        dic_ingredientes = {}
        stock_nombres = []
        for linea in archLec:
            nombre, cantidad = linea.strip().split(";")
            stock_nombres.append (nombre)
        
        while True:
            try: 
                id_plato = str(ingresar_num_mayor_a(1,"Ingrese ID del plato: "))
                if id_plato in carta:
                    raise ValueError
                
                break
            except ValueError:
                print ("Error, ID de plato ya existente!")

        plato_a_agregar = str_minimo_n_caracteres(3,"Ingrese el nombre del plato a agregar: ")

        precio = ingresar_valor_float_positivo(f"Ingrese el precio de {plato_a_agregar}: $")

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
        archLec.close()
        return nueva_entrada
    
def guardar_agregar_plato (nueva_entrada):
    try:
        arch = open("carta.json", "rt", encoding="utf-8")
        datos = json.load(arch)
        datos.update(nueva_entrada)

        arch2 = open ("carta.json","wt",encoding="utf-8")
        json.dump (datos,arch2,indent=4)

        print("Plato nuevo agregado correctamente a la carta.")
    except IOError:
        print("Error al guardar la carta.")



# -------------- MENÚ PRINCIPAL-----------------------#

def menu_principal(carta, stock,pedidos):
    print("\n🍷 ----- Menú EntreSabores ----- 🍷")
    print(" 1️⃣  🧾 Tomar pedido")
    print(" 2️⃣  💵 Cerrar mesa")
    print(" 3️⃣  📜 Mostrar carta")
    print(" 4️⃣  📦 Mostrar stock de ingredientes")
    print(" 5️⃣  ✏️ Modificar carta")
    print(" 6️⃣  📊 Ver reportes")
    print(" 0️⃣  🚪 Salir")

    opcion = numeroEntreRango(0, 5, "Ingrese una opción: ")

    if opcion == 1:
        registrar_evento("Tomar pedido")
        pedido = tomar_pedido(carta, stock,pedidos)
        menu_principal(carta, stock,pedidos)
    elif opcion == 2:
        registrar_evento("Cerrar mesa")
        #cerrar_mesa(pedidos)
    elif opcion == 3:
        registrar_evento("Mostrar carta")
        mostrar_carta(carta,stock,pedidos)
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
        # ver_reportes()





