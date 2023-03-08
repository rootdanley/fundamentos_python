def contar_digitos(numero):
    qtd_digitos = 0
    while numero > 0:
        qtd_digitos += 1
        numero = numero // 10
    return qtd_digitos

numero = int(input("Digite um número inteiro: "))

qtd_digitos = contar_digitos(numero)

print("O número", numero, "tem", qtd_digitos, "dígitos.")
