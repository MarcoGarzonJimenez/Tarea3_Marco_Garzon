# Solicitar el nivel de glucosa al usuario
glucosa = float(input("Ingrese el nivel de glucosa en ayunas (mg/dL): "))

# Evaluar el nivel de glucosa según los criterios médicos
if glucosa <= 65:
    print("\nResultado: HIPOGLICEMIA")
    print("Criterio: Nivel de glucosa menor o igual a 65 mg/dL")
elif glucosa > 65 and glucosa < 100:
    print("\nResultado: NORMAL")
    print("Criterio: Nivel de glucosa mayor a 65 mg/dL y menor a 100 mg/dL")
elif glucosa >= 100 and glucosa <= 110:
    print("\nResultado: PREDIABETES")
    print("Criterio: Nivel de glucosa entre 100 y 110 mg/dL")
else:
    print("\nResultado: DIABETES")
    print("Criterio: Nivel de glucosa mayor a 110 mg/dL")