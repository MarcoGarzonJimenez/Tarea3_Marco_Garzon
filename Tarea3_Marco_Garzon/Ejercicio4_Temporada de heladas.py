# Solicitar la temperatura al usuario
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

# Evaluar la temperatura con condicionales anidados
if temperatura <= 6:
    print("\nResultado: TEMPORADA DE HELADAS")
    print("Criterio: Temperatura menor o igual a 6 grados")
else:
    if temperatura < 12:
        print("\nResultado: TEMPORADA PRÓXIMA A HELADAS")
        print("Criterio: Temperatura mayor a 6 y menor a 12 grados")
    else:
        print("\nResultado: NO HAY TEMPORADA DE HELADAS")
        print("Criterio: Temperatura mayor o igual a 12 grados")