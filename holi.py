import chao as funcion

usuario1="calfun"
contraseña1="123"
usuario2="juany"
contra2="1234"          

eleccion_salir=0

print("\nBienvenido a plataforma de registro de trabajadores")

while True:
    user=input("\nIngresar usuario: ")
    passw=input("Ingresar contraseña: ")
    
    if user==usuario1 and passw==contraseña1 or user==usuario2 and passw==contra2:
        break
    else:
        print("\nDatos ingresados invalidos")

while True:
    print("\n1. Registrar trabajador")
    print("2. Listar los todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del Programa")

    while True:
        try:
            eleccion_menu=int(input("\nOpción -> "))
        except ValueError:
            print("\nOpción invalida")
        else:
            if eleccion_menu==1:
                print("\nRegistrar trabajador")
                #rellenar con funcion
                funcion.ingresaTrabajador();
                break

            elif eleccion_menu==2:
                print("\nListar los todos los trabajadores")
                #rellenar con funcion
                funcion.listarTrabajadores();                  
                break

            elif eleccion_menu==3:
                print("\nImprimir planilla de sueldos")
                #rellenar con funcion
                funcion.imprimirPlanilla();
                break

            elif eleccion_menu==4:
                while True:
                    print("\n¿Está seguro que desea salir?")
                    
                    print("\n1. Sí")
                    print("2. No")
                    
                    try:
                        eleccion_salir=int(input("Opción -> "))
                    except ValueError:
                        print("\nOpción invalida")
                    else:
                        if eleccion_salir==1:
                            break
                        elif eleccion_salir==2:
                            break
                        else:
                            print("\nOpción invalida")

                if eleccion_salir==1 or eleccion_salir==2:
                    break

            else:
                print("\nOpción invalida")

    if eleccion_salir==1:
        break