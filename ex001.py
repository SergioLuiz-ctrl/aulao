# Joaozinho quer calcular e mostrar a quantidade de litros de combustivel gastos em uma viagem, ao     utilizar um automovel que faz 12KM/L. Para isso, ele gostaria que você o auxiliasse através de um   simples programa. para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a   velocidade média durante a mesma (em KM/h). Assim pode-se obter distância percorrida e, em seguida,   calcular quantos litros seriam necessários. Mostre o valor da quantidade de combustível necessário com  3 casas decimais após o ponto. 

qtddeHoras = int(input("Informe a quantidade de horas de viagem: "))
velocidadeMedia = float(input("Qual foi a velocidade media do veiculo: ")) 

distancia = qtddeHoras * velocidadeMedia
litros = distancia / 12

print("A distncia percorrida e ", distancia)
print(f"A quantidade de litros foi:  {litros:.3}")