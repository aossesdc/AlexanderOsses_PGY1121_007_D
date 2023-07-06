
#precios entradas
platinum = 120000
gold     = 80000
silver   = 50000
#ver menu concierto
def ver_menu_concierto():
    print("""       MENÚ CONCIERTO 
    1.Comprar entradas
    2.Mostrar ubicaciones disponibles
    3.Ver listado asistentes
    4.Mostrar ganancias totales
    5.salir""")
#validar opcion
def validar_opcion():
        opcion=int(input("Ingrese una opción: "))
        try:
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR! Opcion incorrecta ")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO")
#validar rut       
def validar_rut():
        rut=int(input("Ingrese su rut (sin guion,puntos ni dígito verificador): "))
        try:
            if rut >1000000 and rut <99999999:
                print("Su RUT a sido guardado exitosamente")
                return rut
            else:
                print("ERROR! Debe ingresar su rut sin guion,sin puntos ni dígito verificador(8 digitos)")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO")
        
#acumuladores iniciados en 0     
acumulador_platino=0
acumulador_gold=0
acumulador_silver=0
#contador platino
contador_platino=0
contador_gold=0
contador_silver=0
#validar compra entrada
import numpy as np 
concierto=np.zeros((10,10))
def ver_asientos_disponibles():
    if concierto not in 0: 
        print("No Hay asientos disponibles")
    else:
        for x in range(10):
            print(f"FILA{x+1}", end=" ")
            for y in range(10):
                print("COLUMNA 1 2 3 4 5 6 7 8 9 10")
            print("")
        print("")
lista_ruts=[]
lista_entrada=[]
lista_platino=[]
lista_gold=[]
lista_silver=[]

def comprar_entradas():   
            if comprar_entradas():
                rut=validar_rut()  
                entrada=input(f"Entradas (P)PLATINUM${platinum},(G)GOLD${gold},(S)SILVER${silver}")
                if entrada.upper in("P","G","S"):
                    if entrada.upper in("P"):
                        try:
                            cantidad_entradas_p=int(input("Cuantas entradas desea comprar(solo se puede comprar de 1 a 3 entradas): "))
                            if cantidad_entradas_p >=1 and cantidad_entradas_p <=3:
                                acumulador_platino=acumulador_platino+cantidad_entradas_p*120000
                                contador_platino=contador_platino+cantidad_entradas_p
                            else:
                                print("ERROR!Debe ingresar un número entre 1 a 3")
                        except:
                            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO")
                    elif entrada.upper in("G"):
                        try:
                            cantidad_entradas_g=int(input("Cuantas entradas desea comprar(solo se puede comprar de 1 a 3 entradas): "))
                            if cantidad_entradas_g >=1 and cantidad_entradas_g <=3:
                                acumulador_gold=acumulador_gold+cantidad_entradas_g*80000
                                contador_gold=contador_gold+cantidad_entradas_g
                            else:
                                print("ERROR!Debe ingresar un número entre 1 a 3")
                        except:
                            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO")
                    else:
                        try:
                            cantidad_entradas_s=int(input("Cuantas entradas desea comprar(solo se puede comprar de 1 a 3 entradas): "))
                            if cantidad_entradas_s >=1 and cantidad_entradas_s <=3:
                                acumulador_silver=acumulador_silver+cantidad_entradas_s*50000
                                contador_silver=contador_silver+cantidad_entradas_s
                            else:
                                print("ERROR!Debe ingresar un número entre 1 a 3")
                        except:
                            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO")
                    return entrada
                else:
                    print("ERROR! Opcion Incorrecta")           
            lista_ruts.append(rut)         
            lista_entrada.append(entrada)
  
    
    
total_t=acumulador_gold+acumulador_platino+acumulador_silver
can_tot_ent=contador_platino+contador_gold+contador_silver
def ver_ganancias_totales():   
    print("GANANCIAS TOTALES")
    print(f"PLATINUM ${platinum},CANTIDAD {contador_platino},TOTAL ${acumulador_platino}")
    print(f"GOLD ${gold},CANTIDAD {contador_gold},TOTAL ${acumulador_gold}")
    print(f"PLATINUM ${silver},CANTIDAD {contador_silver},TOTAL ${acumulador_silver}")
    print(f"CANTIDAD DE ENTRADAS VENDIDAS {can_tot_ent}, TOTAL DE VENTAS ${total_t}")

def validar_salida():
    print("ALEXANDER OSSES USTED A SALIDO DEL SISTEMA 06/07/2023" )
    
def ver_asistentes():
    print(lista_ruts)
        
