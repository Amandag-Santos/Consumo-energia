
# Entrada dos dados solicitados

print(" Olá, essa é uma calculadora de consumo de energia")

nome_aparelho = input(" Digite o nome do aparelho: ")

potencia_aparelho = float(input(" Digite a potência do aparelho em watts: "))

tempo_uso = float(input(" Digite o tempo médio de uso diário em horas: "))

valor_KWh = float(input(" Digite o valor do KWh (ex: 0.75): "))

# O cálculo é feito: (Potência do aparelho * Tempo de uso diário * 30 dias) /1000

consumo_mensal = float(( potencia_aparelho * tempo_uso * 30 ) /1000 )

custo_mensal = float(( valor_KWh * consumo_mensal ))

print(f" Aparelho: {nome_aparelho} ")
print(f" Consumo estimado: {consumo_mensal:.2f} KWh/mês ")
print(f" Gasto mensal do aparelho: R${custo_mensal:.2f} ")