# PROGRAMA PRINCIPAL - ENTRE SABORES

from funciones import generar_archivo_usuarios, log_in, menu_principal, cargar_menu

def main():
    generar_archivo_usuarios()
    #usuario = log_in()
    cargar_menu() #esto esta asi para probar pero luego hay que asignarlo a una variable para poder trabajr con el dicc
    menu_principal()

if __name__ == "__main__":
    main()