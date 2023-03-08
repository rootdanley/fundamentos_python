def sao_todos_digitos_pares(numero):
    for digito in str(numero):
        if int(digito) % 2 != 0:
            return False
    return True

numeros_pares = []
for numero in range(100, 401):
    if sao_todos_digitos_pares(numero):
        numeros_pares.append(numero)

print(*numeros_pares, sep=", ")
