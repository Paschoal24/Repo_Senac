comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
largura = float(input("Digite a largura da cozinha (em metros): "))
altura = float(input("Digite a altura da cozinha (em metros): "))

area_paredes = 2 * (comprimento + largura) * altura

area_por_caixa = 1.5

caixas_necessarias = int((area_paredes + area_por_caixa - 0.0001) // area_por_caixa)
if area_paredes % area_por_caixa != 0:
    caixas_necessarias += 1

print(f"\nÁrea total das paredes: {area_paredes:.2f} m²")
print(f"Caixas de azulejos necessárias: {caixas_necessarias}")
