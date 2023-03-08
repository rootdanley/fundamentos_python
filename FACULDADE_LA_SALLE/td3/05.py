def ler_numeros():
    numeros = []
    numero = int(input("Digite um número inteiro (0 para sair): "))
    while numero != 0:
        numeros.append(numero)
        numero = int(input("Digite um número inteiro (0 para sair): "))
    return numeros

def somar_numeros(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

numeros = ler_numeros()
soma = somar_numeros(numeros)

print("A soma de todos os números digitados é:", soma)
