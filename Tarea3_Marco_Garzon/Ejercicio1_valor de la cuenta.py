# Solicitar el valor de la cuenta al usuario
valor_cuenta = float(input("Por favor ingrese el valor de la cuenta: "))

# Calcular la propina según el valor de la cuenta
if valor_cuenta <= 50000:
    propina = valor_cuenta * 0.10  # 10% de propina
else:
    propina = valor_cuenta * 0.05  # 5% de propina

# Mostrar el valor de la propina sugerida
print(f"El valor de la propina sugerida es: ${propina:,.2f}")
