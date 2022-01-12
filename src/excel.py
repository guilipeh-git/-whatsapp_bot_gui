# pip install pandas
try:
    def excel(file=""):
        if file != "":
            import pandas as pd



            tabela = pd.read_excel(file)
            fraseErro = lambda : """
                ERROR! Não foi possivel executar sua Planilha do excel
                pois ela não cumpre os requisitos da tabela padrão.
                Padronize sua tabela e tente novamente...
                """
            tbl = lambda x: str(tabela.keys()).lower().find(x) != -1

            def filtra(nome):
                tab = [c  for c in tabela.keys()]
                pos = [rs for rs in range(len(tab)) if str(tab[rs]).lower().strip() == nome]
                
                if len(pos) >= 0:
                    return [tabela[tab[pos[0]]]]

            if tbl("numero"):
                try:
                    try:
                        nomes = [str(nome) for nome in filtra("nome")[0]]
                    except:
                        nomes = [str(nome) for nome in filtra("nomes")[0]]
                        
                    try:
                        num =[str(num) for num in filtra("numero")[0]]
                    except:
                        num =[str(num) for num in filtra("numeros")[0]]
                    trataMsg = lambda x: [str(msg) for msg in filtra(x)[0]]
                    try:
                        msg = trataMsg("mensagem")
                    except:
                        try:
                            msg = trataMsg("menssagem")
                        except:
                            try:
                                msg = trataMsg("mesagem")
                            except:
                                try:
                                    msg = trataMsg("messagem")
                                except:
                                    try:
                                        msg = trataMsg("mesagem")
                                    except:
                                        try:
                                            msg = trataMsg("mesage")
                                        except:
                                            try:
                                                msg = trataMsg("message")
                                            except:
                                                try:
                                                    msg = trataMsg("menssage")
                                                except:
                                                    msg = trataMsg("mensage")
                                                
                    return [f"{nomes[i]}, {num[i].replace('.0','')},{msg[i]}" for i in range(len(num))]
                except:
                    return fraseErro()  
                
            else:
                return fraseErro()
                
                
        if __name__ == "__main__":
            print(excel(file="tabela.xlsx"))
except:
    print("sem excel")