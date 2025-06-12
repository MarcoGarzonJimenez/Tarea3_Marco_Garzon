# Solicitar dos números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostrar opciones de operación
print("\nSeleccione la operación que desea realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicitar la operación
opcion = input("\nIngrese el número de la operación (1-4): ")

# Realizar la operación seleccionada y mostrar el resultado
if opcion == '1':
    resultado = num1 + num2
    print(f"\nEl resultado de la suma es: {resultado}")
elif opcion == '2':
    resultado = num1 - num2
    print(f"\nEl resultado de la resta es: {resultado}")
elif opcion == '3':
    resultado = num1 * num2
    print(f"\nEl resultado de la multiplicación es: {resultado}")
elif opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nEl resultado de la división es: {resultado}")
    else:
        print("\nError: No se puede dividir entre cero")
else:
    print("\nOpción no válida. Por favor seleccione un número del 1 al 4.")