
inicio_odometro = float(input("Marcação do odômetro no início do dia (km): "))
fim_odometro = float(input("Marcação do odômetro no fim do dia (km): "))
litros_consumidos = float(input("Quantidade de litros de combustível consumidos: "))
valor_recebido = float(input("Valor total recebido dos passageiros (R$): "))


preco_combustivel = 4.87


distancia_percorrida = fim_odometro - inicio_odometro


if litros_consumidos > 0:
    media_consumo = distancia_percorrida / litros_consumidos
else:
    media_consumo = 0

gasto_combustivel = litros_consumidos * preco_combustivel

lucro_liquido = valor_recebido - gasto_combustivel

print(f"\nMédia de consumo: {media_consumo:.2f} km/l")
print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")
print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")
