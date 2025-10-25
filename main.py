# PROGRAMA PRINCIPAL - ENTRE SABORES


from funciones import (
    generar_archivo_usuarios,
    log_in,
    menu_principal,
    cargar_carta,
    guardar_carta,
    cargar_stock,
    guardar_stock,
    registrar_evento,
    mostrar_carta,
    submenu_modificar_carta,
    agregar_plato,
    guardar_agregar_plato,
    eliminar_plato,
    modificar_plato,
    mostrar_stock,
    numeroEntreRango,
    ingresar_num_entero,
    ingresar_num_mayor_a,
    ingresar_valor_float_positivo,
    str_minimo_n_caracteres,
    tomar_pedido
)

def main():
    generar_archivo_usuarios()
    #usuario = log_in()
    stock = cargar_stock()
    carta = cargar_carta()
    pedidos = {}

    menu_principal(carta,stock, pedidos)

if __name__ == "__main__":
    main()