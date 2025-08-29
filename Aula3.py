while True:
    try:
        nome= input ("Digite sue nome: ")
        break
    except:
        break
    
while True:
    try:
        noites = int (input("Quantas noites você quer ficar? "))
        break
    except:
        print("voce precisa digitar um numero: ")
        break
while True:
    try:
        print("tipos de quartos: Genin, Jounin ou Hokage")
    except:
        break
    tipo_quarto = input("Digite o tipo de quarto: ")
    

    if tipo_quarto == "Genin":
        preco = 120
        break
    elif tipo_quarto == "Jounin":
        preco = 180
        break
    elif tipo_quarto == "Hokage":
        preco = 250
        break
    else:
        print("Tipo de quarto inválido. Tente novamente.")
