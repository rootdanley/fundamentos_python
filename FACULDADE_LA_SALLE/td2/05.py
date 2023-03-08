def verificar_sexo(letra):
    if letra == "F" or letra == "f":
        print("F - Feminino")
    elif letra == "M" or letra == "m":
        print("M - Masculino")
    else:
        print("Sexo Inválido")
        
letra = input("Digite uma letra para verificar o sexo correspondente: ")
verificar_sexo(letra)
