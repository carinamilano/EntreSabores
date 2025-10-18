# MÓDULO DE FUNCIONES - ENTRESABORES

from datetime import datetime
import json

# LOGIN Y USUARIOS
def log_in():
    while True:
        usuario = input("Ingrese usuario: ")
        contrasena = input("Ingrese contraseña: ")
        encontrado = False
        try:
            arch = open("usuarios.txt", "rt")
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


#funcion GENERICA para validar un ingreso de un num entero dentro de un rango
def numeroEntreRango(num1, num2, texto):
    while True:
        try:
            num = int(input(texto))
            if num < num1 or num > num2:
                raise ValueError
            return num
        except ValueError:
            print("Error, debe ingresar opción válida")
            continue


#el log
def registrar_evento(opcion, archivo="registros_eventos.txt"):
    try:
        marca = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arch = open(archivo, "at")
        arch.write(marca + ";" + opcion + ";" + "\n")
        arch.close()
    except IOError:
        print("No se pudo crear registro de logs")

def mostrar_carta(): #muestra los platos del menu con sus ingredientes y precio
    try:
        arch=open("menu.json","rt", encoding="utf-8")
        menu=json.load(arch)
        arch.close()
        print("\n📜 ----- CARTA DE PLATOS ----- 📜")
        for plato, datos in menu.items():
            print(f"\n🍽️ {plato.upper()}")
            print(f"   💲 Precio: ${datos["precio"]:.2f}")
            print(f"   🏷️ Tipo: {datos["tipo"]}")
            print(f"   🧂 Ingredientes:{datos["ingredientes"]}")
        print("\n")
        print("\n")

    except IOError:
        print("Error con los archivos")


#menu principal
def menu_principal():
    print("🍽️ ----- Menú EntreSabores ----- 🍷")
    print("1️⃣  📜 Mostrar carta")  # platos / precio / ingredientes / tipo
    print("2️⃣  🧺 Mostrar stock de ingredientes")
    print("3️⃣  ✏️  Modificar carta")  # submenú con agregar / eliminar / modificar
    print("4️⃣  📊 Ver reportes")
    print("0️⃣  🚪 Salir")

    opcion = numeroEntreRango(0, 5, "Ingrese una opción: ")

    if opcion == 1:
        registrar_evento("Mostrar carta")
        mostrar_carta()
        menu_principal()
        # mostrar_carta()
    elif opcion == 2:
        registrar_evento("Mostrar stock de ingredientes")
        menu_principal()
        # mostrar_stock()
    elif opcion == 3:
        registrar_evento("Modificar carta")
        # modificar_carta()
    elif opcion == 4:
        registrar_evento("Ver reportes")
        # ver_reportes()

# GESTIÓN DEL MENÚ JSON
def cargar_menu():
#Carga el menú desde menu.json. Si no existe, crea un menú base con 10 platos iniciales
    try:
        arch = open("menu.json", "rt", encoding="utf-8")
        menu = json.load(arch)
        arch.close()
    except FileNotFoundError:
        print("No se encontró menu.json. Creando archivo con menú base...")
        menu = {
            "Milanesa con papas": {
                "precio": 35500.00,
                "ingredientes": {"carne": 1, "huevo": 1, "pan rallado": 1, "papas": 2},
                "tipo": "carnívoro"
            },
            "Pizza muzzarella": {
                "precio": 39500.50,
                "ingredientes": {"harina": 1, "queso": 1, "tomate": 1},
                "tipo": "vegetariano"
            },
            "Bowl de quinoa": {
                "precio": 41500.00,
                "ingredientes": {"quinoa": 1, "zanahoria": 1, "brócoli": 1},
                "tipo": "vegano"
            },
            "Hamburguesa veggie": {
                "precio": 38500.75,
                "ingredientes": {"soja": 1, "pan": 1, "lechuga": 1, "tomate": 1},
                "tipo": "vegetariano"
            },
            "Tarta de calabaza": {
                "precio": 36500.00,
                "ingredientes": {"calabaza": 1, "huevo": 1, "masa": 1, "queso": 1},
                "tipo": "vegetariano"
            },
            "Ensalada César": {
                "precio": 35200.00,
                "ingredientes": {"pollo": 1, "lechuga": 1, "queso": 1, "croutons": 1},
                "tipo": "carnívoro"
            },
            "Sopa de lentejas": {
                "precio": 37200.50,
                "ingredientes": {"lentejas": 1, "zanahoria": 1, "cebolla": 1, "ajo": 1},
                "tipo": "vegano"
            },
            "Risotto de hongos": {
                "precio": 46500.00,
                "ingredientes": {"arroz": 1, "hongos": 1, "crema": 1, "queso": 1},
                "tipo": "vegetariano"
            },
            "Pollo al curry": {
                "precio": 52500.00,
                "ingredientes": {"pollo": 1, "curry": 1, "arroz": 1, "crema": 1},
                "tipo": "carnívoro"
            },
            "Tacos de maíz": {
                "precio": 39800.00,
                "ingredientes": {"maíz": 1, "palta": 1, "porotos": 1, "cebolla": 1},
                "tipo": "celíaco"
            }
        }
        guardar_menu(menu)
    return menu

def guardar_menu(menu):
#Guarda el menú actualizado en el archivo JSON
    try:
        arch = open("menu.json", "wt", encoding="utf-8")
        json.dump(menu, arch, indent=4, ensure_ascii=False) #dump="vuelca,graba", ensure_ascii=False: No conviertas los caracteres acentuados a códigos Unicode, dejalos tal cual
        arch.close()
        print("Menú guardado correctamente.")
    except IOError:
        print("Error al guardar el menú.")