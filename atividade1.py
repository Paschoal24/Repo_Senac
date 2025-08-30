import math


def calcular_iluminacao(potencia_lampada, largura, comprimento):
   
    area = largura * comprimento
    
    
    potencia_necessaria = area * 3
    
   
    num_lampadas =  int (potencia_necessaria / potencia_lampada)
    
    return area, potencia_necessaria, num_lampadas


def verificar_potencia(potencia_lampada):
    if potencia_lampada <= 0:
        return "Potência inválida. A potência da lâmpada deve ser maior que 0 watts."
    elif potencia_lampada <= 10:
        return "Potência baixa, pode não ser suficiente para ambientes grandes."
    elif potencia_lampada <= 50:
        return "Potência média, boa para ambientes de tamanho moderado."
    else:
        return "Potência alta, ideal para grandes ambientes ou para áreas muito iluminadas."


potencia_lampada = float(input("Digite a potência da lâmpada (em watts): "))
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))


potencia_status = verificar_potencia(potencia_lampada)
print(potencia_status)


if potencia_lampada > 0:
    area, potencia_necessaria, num_lampadas = calcular_iluminacao(potencia_lampada, largura, comprimento)
    
   
    print(f"\nÁrea do cômodo: {area:.2f} m²")
    print(f"Potência total necessária: {potencia_necessaria:.2f} watts")
    print(f"Número de lâmpadas necessárias: {num_lampadas}")
else:
    print("Por favor, insira uma potência de lâmpada válida.")
