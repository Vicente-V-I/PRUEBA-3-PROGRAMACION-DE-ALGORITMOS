#BUSQUEDA POR MODELO / MARCA - 1

def modelo_marca_busqueda(autos):
    modelo_marca = input("Qué modelo o marca de vehiculo está usted interesado?: ")
    encontrados = []
    for auto in autos:
        if modelo_marca.lower() in [auto[1].lower(), auto[0].lower()]:
            encontrados.append(auto)
    if encontrados:
        for auto in encontrados:
            print("Marca:", auto[0])
            print("Modelo:", auto[1])
            print("Año:", auto[2])
            print("Patente:", auto[3])
            print("Color:", auto[4])
    else:
        print("Nuestro sistema no encuentra vehiculos con la marca y/o modelo que usted ha especificado.")

#IMPRESION DE CERTIFICADO - 2

def impresion_de_certificado(autos, nombre_usuario, fecha_de_hoy):
    modelo_marca_busqueda(autos)
    patente = input("Indique la patente del vehiculo seleccionado: ")
    color = input("Indique el color del vehiculo seleccionado: ")
    print(nombre_usuario, "ha emitido el siguiente certificado que indica que:")
    for auto in autos:
        if patente.lower() == auto[3].lower():
            print("El vehículo", auto[0], auto[1], "con patente", auto[3])
            print("de color:", color)
            print("Se ha registrado en nuestro sistema el día", fecha_de_hoy)
            break
    else:
        print("El sistema no encuentra vehiculos con la patente indicada por el usuario.")

#BUSQUEDA POR PATENTE - 3

def patente_busqueda(autos):
    patente = input("Indique la patente que busca: ")
    encontrados = []
    for auto in autos:
        if patente.lower() == auto[3].lower():
            encontrados.append(auto)
    if encontrados:
        for auto in encontrados:
            print("Marca:", auto[0])
            print("Modelo:", auto[1])
            print("Año:", auto[2])
            print("Patente:", auto[3])
            print("Color:", auto[4])
    else:
        print("El sistema no encuentra vehiculos con la patente indicada por el usuario.")


#BUSQUEDA POR COLOR FAVORITO - 4

def color_favorito_busqueda(autos, color_favorito):
    encontrados = []
    for auto in autos:
        if color_favorito.lower() == auto[4].lower():
            encontrados.append(auto)
    if encontrados:
        for auto in encontrados:
            print("Marca:", auto[0])
            print("Modelo:", auto[1])
            print("Año:", auto[2])
            print("Patente:", auto[3])
            print("Color:", auto[4])
    else:
        print("Lo sentimos, en nuestro sistema no se encuentran vehiculos de su color favorito.")

#LISTA DE AUTOS DE IZQUIERDA A DERECHA: MARCA, MODELO, AÑO, PATENTE, COLOR

def main():
    autos = [
        ["Toyota", "GT86", "2016", "RDU243", "Rojo"],
        ["Mitsubishi", "Lancer", "1996", "RNA741", "Rojo"],
        ["Honda", "Civic Type-R", "2005", "QNE248", "Rojo"],
        ["Ferrari", "California", "2014", "FWM618", "Rojo"],
        ["Ferrari", "575M Maranello", "2004", "HIR719", "Azul"],
        ["Honda", "Accord", "1988", "EHP775", "Burdeo"],
        ["Toyota", "Supra", "2023", "DVT712", "Amarillo"],
        ["Honda", "Fit", "2020", "JAE691", "Amarillo"],
        ["Toyota", "4Runner", "1984", "RSB197", "Verde"],
        ["Toyota", "Corolla", "2018", "NQE146", "Morado"],
        ["Toyota", "Yaris", "2020", "ZAV269", "Burdeo"],
        ["Toyota", "Supra", "2021", "UCE557", "Verde"],
        ["Toyota", "4Runner", "2017", "CIF927", "Blanco"],
        ["Honda", "Logo", "1998", "CSX826", "Morado"],
        ["Toyota", "Yaris", "2014", "UHN783", "Verde"],
        ["Toyota", "GT86", "2013", "PXR919", "Burdeo"],
        ["Honda", "Quint", "1985", "HMH396", "Blanco"],
        ["Ferrari", "F430", "2006", "TTH289", "Rojo"],
        ["Toyota", "4Runner", "1990", "VQR314", "Rojo"],
        ["Toyota", "4Runner", "2011", "ASC378", "Azul"]
    ]

#ENTRADA AL SISTEMA

    nombre_usuario = input("Indique su nombre de usuario: ")
    fecha_actual = input("Indique la fecha del dia de hoy: ")
    color_favorito = input("Indique su color favorito: ")

#MENU

    while True:
        print("\nMENU:")
        print("1 - Buscar un automóvil por Modelo / Marca")
        print("2 - Imprimir Certificado")
        print("3 - Buscar automóviles por patente")
        print("4 - Mostrar automóviles del color favorito")
        print("5 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            modelo_marca_busqueda(autos)
        elif opcion == "2":
            impresion_de_certificado(autos, nombre_usuario, fecha_actual)
        elif opcion == "3":
            patente_busqueda(autos)
        elif opcion == "4":
            color_favorito_busqueda(autos, color_favorito)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
