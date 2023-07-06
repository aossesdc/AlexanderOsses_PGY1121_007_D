import funciones as fn
import os
while True:
    os.system('cls')
    fn.ver_menu_concierto()
    opcion=fn.validar_opcion()
    if opcion==1:
        fn.comprar_entradas
    elif opcion()==2:
        fn.ver_asientos_disponibles()
    elif opcion()==3:
        fn.ver_asistentes()
    elif opcion()==4:
        fn.ver_ganancias_totales()
    else:
        fn.validar_salida()
        