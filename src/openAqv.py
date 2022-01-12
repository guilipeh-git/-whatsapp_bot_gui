
def open_aqv(nome_aqv):
    try:
        arquivo = open(nome_aqv,"r")
        print("arquivo  txt existe")
        
    except:
        arquivo = open(nome_aqv,"w")
        print("arquivo criado")
    arquivo.close()


def arquivoNum(contatos,fun="null"):
    
    open_aqv("lista_nums.txt")
    arquivo = open("lista_nums.txt","w")
    if str(fun).lower() == "salvar":
        for num in contatos:
            arquivo.write(str(num)+"\n")
        
    if str(fun).lower() == "ler":
        [print(numero) for numero in open("lista_nums.txt","r")]
    
    arquivo.close()
    
if __name__ == "__main__":
    contats = [99819899,56789021]
    funcao = "ler"
    arquivoNum(contats,funcao)