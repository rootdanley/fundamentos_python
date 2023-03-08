def trocar_valores(var1, var2):
    var1, var2 = var2, var1
    return var1, var2

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

num1, num2 = trocar_valores(num1, num2)

print("Valores trocados: num1 =", num1, "e num2 =", num2)
