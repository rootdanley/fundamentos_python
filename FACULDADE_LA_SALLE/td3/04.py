senha1 = input("Digite a senha: ")
senha2 = input("Confirme a senha: ")

while senha1 != senha2:
    print("As senhas não correspondem. Tente novamente.")
    senha1 = input("Digite a senha: ")
    senha2 = input("Confirme a senha: ")

print("Senha cadastrada com sucesso!")
