#Caluladora basica

#HACE UN CLONADO DE EL SIGNO "=" X 80
LINEA_DOBLE:str = '='*80

#MENU DE LA CALCULADORA
print(LINEA_DOBLE)
print("CALCULADORA BASICA")
print(LINEA_DOBLE)
print("1- SUMA")
print("2- RESTA")
print("3- MULTIPLICACION")
print("4- DIVISION")
print(LINEA_DOBLE)
op = int(input("Seleccione una opcion: "))

#INGRESO DE DATOS

n1 = int(input("Ingrese el primer valor: "))
n2 = int(input("Ingrese el segundo valor: "))

#Proceso usando bucle if
if op == 1:
    print(f"El resultado de la Suma es: {n1 + n2}")
elif op == 2:
    print(f"El resultado de la Resta es: {n1 - n2}")
elif op == 3:
    print(f"El resultado de la Multiplicacion es: {n1 * n2}")
elif op == 4:
    print(f"El resultado de la Division es: {n1 / n2}")
else:
    print("No existe esa opcion")
    