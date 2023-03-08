

def verificar_nome(nome):
    nome_correto = "danley"  # nome pré-definido
    if nome == nome_correto:
        print("Nome correto!")
    else:
        print("Nome incorreto!")
        
nome_usuario = input("Digite seu nome: ").lower()
verificar_nome(nome_usuario)
