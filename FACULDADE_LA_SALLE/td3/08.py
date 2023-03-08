def calcular_soma_media():
    numeros = []
    numero = int(input("Digite um número (0 para terminar): "))
    while numero != 0:
        numeros.append(numero)
        numero = int(input("Digite um número (0 para terminar): "))
    
    if len(numeros) == 0:
        print("Não foram digitados números.")
    else:
        soma = sum(numeros)
        media = soma / len(numeros)
        print(f"Soma: {soma}")
        print(f"Média: {media}")

calcular_soma_media()
