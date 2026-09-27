#consumo de energia

#coletando os dados
nome_aparelho = input("Digite o nome do aparelho: ")

potencia = float(input("Digite a potência do aparelho em Watts(W): "))

tempo_de_uso = float(input("Digite o tempo médio de uso diário em horas do aparelho: "))


#realizando os cálculos
consumoMensal = (potencia * tempo_de_uso * 30) / 1000


#saída dos dados
print("Aparelho:",nome_aparelho)

print("Consumo estimado:",consumoMensal,"KWh / mês")


