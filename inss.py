salario_bruto = float(input("Digite o valor do salário bruto: "))
horas = float(input("Digite quantas horas extras: "))
valor_horas = float(input("Digite o valor das horas extras: "))
inss = ((horas * valor_horas) + salario_bruto) * 8 / 100
print(salario_bruto - inss)
