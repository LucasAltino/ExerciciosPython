salario = float(input("Digite o valor do seu salário: "))
aumento = float(input("Digite o pencentual de aumento:"))
novo = salario + (salario/100 * aumento)

print("O valor de seu salário será de:", novo)