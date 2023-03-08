def calcula_valor_total(valores):
    valor_total = sum(valores)
    if valor_total > 1000:
        valor_total = valor_total * 0.9
    return valor_total

valores = []
while True:
    valor = float(input("Digite o valor do produto (digite 0 para sair): "))
    if valor == 0:
        break
    elif valor < 0:
        print("Valor inválido, tente novamente.")
    else:
        valores.append(valor)

valor_total = calcula_valor_total(valores)
print(f"O valor total a pagar é: R$ {valor_total:.2f}")
