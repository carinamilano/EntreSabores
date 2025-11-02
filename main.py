"""PROYECTO FINAL - PROGRAMACIÓN 1
Sistema de gestión gastronómica “EntreSabores”
UADE - Segundo Cuatrimestre 2025

Fecha: Noviembre 2025

Descripción general:
El sistema permite administrar las operaciones de un restaurante desde consola.
Incluye:
- Gestión de carta de platos y stock de ingredientes.
- Toma y cierre de pedidos por mesa.
- Generación automática de reportes estadísticos.
- Módulo de login y usuarios con contraseñas almacenadas en archivo de texto.
- Control de errores mediante manejo de excepciones.
- Uso de estructuras de datos: listas, diccionarios y funciones lambda.
- Creación y actualización de múltiples archivos CSV y TXT.

Estructura modular del proyecto:
--------------------------------
📂 main.py → Contiene el menú principal, control del flujo y llamadas a módulos.
📂 funciones.py → Implementa las operaciones CRUD sobre carta, stock y usuarios.
📂 reportes.py → Genera reportes estadísticos (ventas, ingredientes, platos, tipos).
📂 carta.json → Archivo base de platos y precios.
📂 stock.csv → Control de insumos e inventario.
📂 usuarios.txt → Base de usuarios y contraseñas.
📂 ventas.csv → Registro de ventas simuladas o reales.
📂 registros_eventos.txt → Bitácora de acciones y eventos del sistema.

Requerimientos funcionales cubiertos:
-------------------------------------
1️⃣ Login de usuario válido (archivo de texto con contraseñas).
2️⃣ Menú principal con validación por excepciones.
3️⃣ Generación automática de archivos de entrada con datos aleatorios.
4️⃣ Uso de diccionarios y listas para agrupar datos.
5️⃣ Creación de al menos cuatro archivos nuevos de salida
(tipos_consumidos.csv / ventas_horarias.csv / ingredientes_top.csv / platos_top.csv)
"""


from funciones import (
    generar_archivo_usuarios,
    log_in,
    menu_principal,
    cargar_carta,
    guardar_carta,
    cargar_stock,
    agregar_nuevo_ingrediente,
    guardar_stock,
    registrar_evento,
    mostrar_carta,
    submenu_modificar_carta,
    agregar_plato,
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
    usuario = log_in()
    stock = cargar_stock()
    carta = cargar_carta()
    pedidos = {}
    menu_principal(carta,stock, pedidos)

if __name__ == "__main__":
    main()