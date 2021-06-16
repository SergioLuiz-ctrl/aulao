# Faça um algoritmo para ler o sálario de um funcionário e aumentá-lo em 15%. Após o aumento , o salario final, o desconto do INSS, o desconto do FGTS e o total de descontos


salario = float(input("Digite seu salario R$ "))

salReajustado = (salario * 0.15) + salario

print("O salario reajustado e R$ ", salReajustado)

inss = salReajustado * 0.11
fgts = salReajustado * 0.08

print("Desconto INSS R$ ", inss)
print("Desconto FGTS R$ ", fgts)

desconto = inss - fgts

print(f"Total de Desconto INSS+FGTS R$ {desconto:.3}")
salarioFinal = salReajustado - desconto
print("Salario Final R$ ", salarioFinal)