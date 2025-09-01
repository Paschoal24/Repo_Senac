nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))


notas = [nota1, nota2]

if optativa != -1:
    menor_nota = min(notas)
    if optativa > menor_nota:
        notas[notas.index(menor_nota)] = optativa

media = sum(notas) / 2

print(f"\nMédia final: {media:.1f}")

if media >= 6.0:
    print("Situação: Aprovado")
elif media < 3.0:
    print("Situação: Reprovado")
else:
    print("Situação: Recuperação")
