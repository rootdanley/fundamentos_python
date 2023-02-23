# Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar
numero = int(input("Digite o numero: "))


def num_inteiro(numero):
    if numero % 2 == 0:
        print("É par")
    else:
        print("É impar")


num_inteiro(numero)



