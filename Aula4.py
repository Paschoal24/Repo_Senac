'''numero = ''

while numero != '10':
    senha = input ('Digite o numero: ')
    if senha != '11':
        print('Número incorreto. Digite novamente')

print('Acesso liberado')  ''' 


'''for i in range (0,33,10):
     print(i)'''

'''while True:
    numero = int(input("Digite um número maior que 10: "))

    if numero > 10:
        break  # número válido → sai do loop
    else:
        print("Número inválido. Tente novamente.")

print("Obrigado! Você digitou:", numero)
'''

'''for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")'''

'''numero = 0

while numero <= 20:
  print(numero)

numero += 2'''

'''for i in range(0,11):
  print(i)
else:
  print('Feliz ano novo')

  #Imprima todos os números pares entre 10 e 30 usando range().
for i in range(10, 30, 2):
    print (i)'''

'''cliente = ['Bia', 18, 17000, 'Sao cristovão']
print(cliente)

telefone = 21984578078

cliente.append(telefone)

print(cliente)'''

'''cliente = ['Bia', 18, 17000, 'Sao cristovão']
telefone = 137264781

cliente.append(telefone)

for i in cliente:
  print(i)'''

'''cliente= []
while True:
    try:
         num = int(input('Digite o n°: '))
         cliente.append(num)
         sair = input('Deseja inserir mais um numero? (S/N)').upper()
         if sair == 'N':
            break
    except:
         print('Digite um n° válido')'''

'''while True: 
    try: 
        opcao = int(input('opcao: '))
        if opcao in [1,2,3,4]:
            print('opção ok')
            break
        else:
            print('Opção inválida')
    except:
        print('Digite um n° válido: ')'''

nomes = []
valores = []


quantidade = int(input("Quantos produtos você deseja cadastrar? "))


for i in range(quantidade):
    print(f"Produto {i + 1}:")
    
    nome = input("Nome do produto: ")
    valor = float(input("Valor do produto: R$ "))
    
    nomes.append(nome)
    valores.append(valor)


print("RELATÓRIO DE PRODUTOS")
for i in range(quantidade):
    print(f"{i + 1}. {nomes[i]} - R$ {valores[i]:.2f}")
