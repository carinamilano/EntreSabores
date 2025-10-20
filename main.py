# PROGRAMA PRINCIPAL - ENTRE SABORES

from funciones import generar_archivo_usuarios, log_in, menu_principal, cargar_carta,guardar_stock,cargar_stock,mostrar_stock

def main():
    generar_archivo_usuarios()
    #usuario = log_in()
    stock = cargar_stock()
    carta = cargar_carta()
    pedidos = {}

    menu_principal(carta,stock, pedidos)

if __name__ == "__main__":
    main()