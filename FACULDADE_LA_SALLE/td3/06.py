def ler_numeros():
    numeros = []
    numero = int(input("Digite um número inteiro e positivo (0 para sair): "))
    while numero != 0:
        if numero > 0:
            numeros.append(numero)
        else:
            print("Número inválido! Digite novamente.")
        numero = int(input("Digite um número inteiro e positivo (0 para sair): "))
    return numeros

def encontrar_maior(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

numeros = ler_numeros()
if len(numeros) == 0:
    print("Nenhum número foi digitado.")
else:
    maior = encontrar_maior(numeros)
    print("O maior número digitado foi:", maior)
