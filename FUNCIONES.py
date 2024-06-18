
 #se intento skrs skr
encabezadoDsctos=( 'Trabajador' , 'Cargo' , 'Sueldo Bruto' , 'Desc. Salud' , 'Desc. AFP' , 'Liquido a pagar' );

encabezado=[ 'Trabajador' , 'Cargo' , 'Sueldo Bruto' ];

listaTrabajadores=[];

trabajadores=[];

cargo=('CEO','ANALISTA DE DATOS','DESARROLLADOR','ANALISTA');
descuentoSalud=0.07;
descuentoAFP=0.12;
sueldoAFP=0;
sueldoSalud=0;
cargo1=[];


def ingresaTrabajador():
    cargo1=input("Ingrese su cargo: ");
    
    while cargo1 not in cargo:
        print("Cargo no identificado,vuelva a intentarlo")
        cargo1=input("Ingrese su cargo: ");
    
    print("\ncargo ingresado.\n")
    nombre=input("Ingrese su nombre y apellido: ");
    trabajadores.append(nombre);
    trabajadores.append(cargo1);
    sueldo=float(input("Ingrese su sueldo bruto: "));
    trabajadores.append(sueldo);
    listaTrabajadores.append(trabajadores);
    sueldoAFP=sueldo*descuentoAFP;
    sueldoSalud=sueldo*descuentoSalud;
    sueldo_liquido_final=sueldo-(sueldoAFP+sueldoSalud)

        
"""def ingresaTrabajador():
    cargo1=input("Ingrese su cargo: ");
    if cargo1 in cargo:
        print("\ncargo ingresado\n.")
        nombre=input("Ingrese su nombre y apellido: ");
        trabajadores.append(nombre);
        trabajadores.append(cargo1);
        sueldo=int(input("Ingrese su sueldo bruto: "));
        trabajadores.append(sueldo);
        listaTrabajadores.append(trabajadores);
    else:
        print("Cargo no identificado,vuelva a intentarlo")"""
    



def listarTrabajadores():
    print(encabezado);
    print(listaTrabajadores); 




def imprimirPlanilla():    
    pregunta=input('Desea imprimir todos los trabajadores?: ')
    if pregunta=="si":
        with open('archivo_Nuevo.txt','w',encoding='utf-8') as archivo:
         archivo.write(encabezadoDsctos);
         archivo.write(trabajadores);
        with open('archivo_nuevo.txt','r',encoding='utf-8') as archivo:
         print(archivo.read());       
    elif pregunta=="no":
        pregunta2=input("que cargo de trabajador desea imprimir: ")
        if pregunta2 in cargo1:
           print(pregunta2);
    else:
       print("Opción invalida")

       #se intento skrs skr
        
        
