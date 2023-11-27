from os import system
system ("cls")

tipos = []
Patentes = []
Marcas = []
Precios = []
Multas = []
Dueños = []
Fechas = []


def Grabar():
    while True:
            tipo = input("-Auto\n-Camioneta\n-Suv\nEscriba porfavor:")
            if tipo.lower() == "auto" or tipo.lower() == "camioneta" or tipo.lower() == "suv":
                print("Ingresado correctamente!")
                tipos.append(tipo)
                break
            else:
                print("opción incorrecta...")
    while True:
        try:
            patente = input("Ingrese la patente, (debe contener números y letras sin guion ni puntos): ")
            if len(patente) <= 6:
                Patentes.append(patente)
                break
            else:
                print("Error, reintente...")
        except:
            print("Ha ocurrido una expción...")
    while True:
            marca = str(input("Ingrese la marca que es el vehiculo: "))
            if len(marca) > 2 or len(marca) <= 15:
                print("Marca ingresada correctamente!")
                Marcas.append(marca)
                break
            else:
                print("Mal ingresado, deben ser minimo 2 chr y max 15 chr...")

    while True:
        try:
            precio = int(input("Ingrese el precio del vehiculo: "))
            if precio >= 5000000:
                Precios.append(precio)
                break
            else:
                print("El valor del auto debe ser mayor a $5.000.000")
        except:
            print("Excepción..., deben ser valores enteros.")

    while True:
        try:
            multa = int(input("Ingrese el monto de la multa: "))
            if multa > 0:
                print("Ingresado correctamente...")
                Multas.append(multa)
            break
        except:
            print("Ha ocurrido una excepción...")

    while True:
        try:
            fecha = input("Ingrese la fecha del registro de su vehiculo: (Ejemplo 21-07-2009):")
            if len(fecha) <= 10:
                print("Ingresado correctamente!!")
                Fechas.append(fecha)
                break
            else:
                print("Fecha mal ingresada...")
        except:
            print("Excepción, deben ser número...")

    while True:
        try:
            dueño = str(input("Ingrese su nombre: "))
            if len(dueño) > 4:
                print("Nombre ingresado correctamente!")
                Dueños.append(dueño)
                break
            else:
                print("Nombre mal ingresado...")
        except:
            print("Excepción deben ser solo caracteres para ingresar el nombre...")


def Buscar():
        while True:
            patente = input("Ingrese la patente para buscarla: ")
            if patente in Patentes:
                index = Patentes.index(patente)
                print("*********VEHICULO ENCONTRADO*********")
                print(f"PATENTE                    :{Patentes[index]}")
                print(f"DUEÑO                      :{Dueños[index]}")
                print(f"TIPO                       :{tipos[index]}")
                print(f"MARCA                      :{Marcas[index]}")
                print(f"PRECIO                     :{Precios[index]}")
                print(f"FECHA REGISTRO             :{Fechas[index]}")
                print(f"MULTA                      :{Multas[index]}")
                break
            else:
                print("Patente no encontrada...")

def ImprimirCertfic():
    while True:
        if not Patentes:
            print("No hay certficados por imprimir: ")
            return
        for i in range (len(Patentes)):
            print("**********Certificados De emisión**********")
            print(f"Certificado       : Dueño de vehiculo{i + 1}")
            print(f"Patente           :{Patentes[i]}")
            print(f"Dueño             :{Dueños}")
            print(f"TIPO AUTO         :{tipos}")
            print(f"MARCA             :{Marcas}")
            print(f"PRECIO            :{Precios}")
            print(f"FECHA REGISTRO    :{Fechas}")
            print(f"MULTA             :{Multas}")
            break

while True:
    print("***********************AUTO SEGURO***********************\n[1]-Grabar\n[2]-Buscar\n[3]-Imprimir Certificados\n[4]-Salir")
    op = input("Ingrese una opción: ")
    if op == "4":
        print("Saliendo del sistema...")
        break
    elif op == "1":
        Grabar()
    elif op == "2":
        Buscar()
    elif op == "3":
        ImprimirCertfic()
    else:
        print("Opción incorrecta, reingrese...")

