from datetime import datetime

def log_in():
    while True:
        usuario = input("Ingrese usuario: ")
        contrasena = input("Ingrese contraseña: ")

        encontrado = False

        try:
            arch = open("usuarios.txt", "rt")
        except IOError:
            print("Error! No se pudo abrir el archivo de usuarios")
            return None
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
        archUsuarios = open("usuarios.txt","wt")
    except IOError:
        print ("No se pudo crear archivo")
    else:
        for usuario in dic_usuario:
            archUsuarios.write (f"{usuario};{dic_usuario[usuario]}\n")
        archUsuarios.close()

def numeroEntreRango(num1,num2,texto):
    while True: 
        try:
            num = int (input(texto))
            if num < num1 or num > num2:
                raise ValueError
            break

        except ValueError:
            print ("Error, debe ingresar opción válida")
            continue
    return num

def registrar_evento(opcion, archivo="registros_eventos.txt"):
    try:
        marca = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arch = open (archivo, "at")
        arch.write (marca+";"+opcion+";"+"\n")
    except IOError:
        print ("No se pudo crear registro de logs")
    arch.close()
    

def mostrar_menu():
    print ("-----Menú EntreSabores-----")
    print ("1. Inicializar sistema") # genera archivos
    print ("2. Mostrar carta") # platos / precio / ingrediente / tipo
    print ("3. Mostrar Stock de ingredientes")
    print ("4. Modificar Carta") # submenú con Agregar plato / eliminar plato / modificar precio
    print ("5. Ver reportes")
    print ("0. Salir")

    opcion = numeroEntreRango (0,5,"Ingrese una opción: ")

    if opcion <0 or opcion >5:
        raise ValueError
    
    if opcion == 1:
        registrar_evento ("Inicializar sistema")
        mostrar_menu()
        #inicializar_sistema()
    elif opcion == 2:
        registrar_evento ("Mostrar carta")
        mostrar_menu()
        #mostrar_carta()
    elif opcion == 3:
        registrar_evento ("Mostrar stock de ingredientes")
        mostrar_menu()
        #mostrar_stock()
    elif opcion == 4:
        registrar_evento ("Modificar carta")
        #modificar_carta()
    elif opcion == 5:
        registrar_evento ("Ver reportes")
        #ver_reportes()

    print ("FIN")                

def main():
    generar_archivo_usuarios()
    usuario = log_in ()
    mostrar_menu()

main()