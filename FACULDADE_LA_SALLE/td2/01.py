# 1. Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas e minúsculas
# b) Quantas letras ao todo
# c) Quantas letras tem o primeiro nome


nome_completo = input("Digite seu nome completo: ")

# Imprime o nome com todas as letras maiúsculas
print("Nome em letras maiúsculas:", nome_completo.upper())

# Imprime o nome com todas as letras minúsculas
print("Nome em letras minúsculas:", nome_completo.lower())

# Calcula o número total de letras do nome
total_letras = len(nome_completo.replace(" ", ""))
print("Total de letras no nome:", total_letras)

# Calcula o número de letras do primeiro nome
primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)
print("Número de letras no primeiro nome:", letras_primeiro_nome)
