
usuario1="usuarioABC"
contraseña1="12345"

print("\nBienvenido plataforma gey xd")

while True:
    user=input("\nIngresar usuario: ")
    passw=input("\nIngresar contraseña: ")
    
    if user==usuario1 and passw==contraseña1:
        break
    else:
        print("Datos ingresados invalidos")

while True
    print("\nMenú de erecciones")

    print("\n1. Registrar trabajador")
    print("2. Listar los todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del Programa gay")

    #agregar try
    eleccion_menu=int(input("\nOpción -> "))

    if eleccion_menu==1:
        print("\nRegistrar trabajador")

    elif eleccion_menu==2:
        print("\nListar los todos los trabajadores")

    elif eleccion_menu==3:
        print("\nImprimir planilla de sueldos")

    elif eleccion_menu==4:
        while True:
            print("\n¿Está seguro que desea salir?")
            
            print("\n1. Sí")
            print("2. No")
            
            eleccion_salir=int(input("Opción -> "))

            if eleccion_salir==1:
                break
            elif eleccion_salir==2:
                break
            else:
                print("\nOpción invalida")

    else:
        print("\nOpción invalida")