frase = str(input("Digite algo: "))
nome = "moises"
teste = frase.lower().find("{nome}")
if(teste != -1):
    print(frase.replace("{nome}",nome))
