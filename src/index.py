#flask==2.0.2

from flask import Flask,render_template,redirect,url_for,request
from openAqv import arquivoNum,open_aqv
from whatsapp import botWhatsapp
import os

app = Flask("__name__")
@app.route("/")
def paginaInicial():
    
    texto = ""
    open_aqv('lista_nums.txt')
    nums = [num for num in open('lista_nums.txt')]
    
    return render_template("index.html",texto = texto)


@app.route("/resp",methods=["POST","GET"])
def respostaPg():
    try:
            os.remove("src/tabela.xlsx")
    except:
        pass
    if(request.method == "POST"):
        listaNum = list()
        textu = request.form["msgHidden"]
        nums = request.form["np"].split(",")
        
        
        try:
            file = request.files.get("file")  
            resp = lambda x : file.filename.lower().find(x)
            if(resp(".xlsx") != -1):
                file.save(os.path.join("src","tabela.xlsx"))
        except:
            pass
            
        
        for num in nums:
            
            #print(num)
            num = str(num).replace(" ","").replace("-","")
            if len(num) == 9:
                num = f"5562{num}"
            if len(num) == 11:
                num = f"55{num}"
                
            if str(num).isnumeric():
                listaNum.append(num.strip()+",")
                #print(listaNum)
                arquivoNum(listaNum,"salvar")
        
        listaNum = [["nan",numero,textu] for numero in listaNum]
        try:
            if(resp(".xlsx") != -1 or len(listaNum) > 0):
                botWhatsapp(listaNum)      
        except:
            print("Ouve uma interrupção na execução do bot.")
        
    return redirect(url_for("paginaInicial"))
    

if(__name__ == "__main__"):
    app.run(host = "0.0.0.0",debug=True, port=80)
