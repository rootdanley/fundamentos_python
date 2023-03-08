def fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n+1):
            resultado *= i
        return resultado

num = int(input("Digite um número para calcular seu fatorial: "))
print("O fatorial de", num, "é", fatorial(num))
