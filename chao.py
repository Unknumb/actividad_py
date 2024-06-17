
encabezado=['Trabajador','Cargo','Sueldo Bruto','Desc. Salud','Desc. AFP','Liquido a pagar'];
trabajadores=[[

]];
cargo=['CEO','Analista de Datos','Desarrollador']

def ingresaTrabajador():
    nombre=input("Ingrese su nombre y apellido: ");
    trabajadores.append(nombre);
    cargo1=input("Ingrese su cargo: ");
    if cargo1==cargo:
        print("cargo ingresado.")
        trabajadores.append(cargo);
        print("Cargo no identificado,vuelva a intentarlo")
    sueldo=int(input("Ingrese su sueldo bruto: "));
    trabajadores.append(sueldo);
   
   
def listarTrabajadores():
    trabajadores()
    



