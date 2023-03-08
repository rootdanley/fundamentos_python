def verificar_vogal_consoante(letra):
    vogais = "aeiouAEIOU"
    if letra in vogais:
        print("A letra digitada é uma vogal!")
    else:
        print("A letra digitada é uma consoante!")
        
letra = input("Digite uma letra para verificar se é vogal ou consoante: ")
verificar_vogal_consoante(letra)
