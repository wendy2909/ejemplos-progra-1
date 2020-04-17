import os
import sys
import json
print("===========================")
print("Bienvenido :)")
print("===========================\n")   
print("Menu:") 
#Aqui empieza el codigo 
#Aqui nos permite ingresar cuantas veces deseamos ingresar al program
#parte 1 realizada por Darsy
veces = int(input('¿cuantas veces desea entrar?'))
for i in range(veces):
    print("1.Ingresar")
    opcion = int(input("Eliga Una opcion"))
    if opcion == 1:
        datos = []
        tipo = input('Tipos de Vehiculos:\n 1. Motocicleta (Q15) \n 2.Automovil (Q30) \n 3.Camioneta (Q50) \n ')
        if tipo == '1':
            precio = 15
            tipos = 'Motocicleta'
        elif tipo == '2': 
            precio = 30
            tipos = 'Automovil'
        elif tipo == '3':
            precio = 50
            tipos = 'Camioneta'
        else: 
            print('Opcion no valida')
#Parte 2: realizada por wendy
        os.system('cls')
        cliente = input('Tipos de Cliente:\n 1.Estandar \n 2.Miembro \n ' )
        if cliente == '1':
            cli = 'Estandar'
            descuentos = 0   
        elif cliente == '2':
            cli = 'Miembro'
            descuentos = precio * 0.10    
        else: 
            print('Opcion no valida')
#regresa producto boleano
        os.system('cls')
        Semana = input('¿Es Fin de Semana: ?\n 1.SI \n 2.NO \n ' )
        if Semana == '1':
            sem = True
            descuentos1 = 0   
        elif Semana == '2':
            sem = False
            descuentos1 = precio * 0.10 
        else: 
            print('Opcion no valida')
            sys.exit()
#Aqui es donde llamamos a las variables para almacenarlas
#crear una clase para almacenar
        for i in range (1): 
            totas_descuentos = descuentos + descuentos1
            total_prec = precio - totas_descuentos
            vehiculos = {}
            vehiculos['tipo:'] = tipos
            vehiculos['precio:'] = precio
            vehiculos['Cliente:'] = cli
            vehiculos['¿Es fin de Semana?:'] = sem
            vehiculos['descuentos:'] = totas_descuentos
            vehiculos['Total:'] = total_prec
            vehiculos['veces'] = veces 
            datos.append(vehiculos)
        print(datos)
#Aqui abrimos json 
with open('datos.json', 'w') as archivo:
    json.dump(datos, archivo)
    print("Exportado con exito")
