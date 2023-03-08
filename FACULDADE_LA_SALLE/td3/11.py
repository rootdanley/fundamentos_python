# a) Usando um loop for e condicional if para verificar se o número é par:


soma_pares = 0
for i in range(2, 101, 2):
    soma_pares += i
print("A soma de todos os números pares entre 2 e 100 é:", soma_pares)

#b) Usando um loop for e elevando cada número ao quadrado:



soma_quadrados = 0
for i in range(1, 101):
    soma_quadrados += i**2
print("A soma de todos os quadrados entre 1 e 100 é:", soma_quadrados)

#c) Usando um loop while e verificando se cada número é ímpar:


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
soma_impares = 0
while a <= b:
    if a % 2 != 0:
        soma_impares += a
    a += 1
print("A soma de todos os números ímpares entre a e b é:", soma_impares)
