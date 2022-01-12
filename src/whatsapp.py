#pip install selenium
#pip install webdriver_manager
def botWhatsapp(listaCont=[["","nan",""]]):
    if listaCont == []:
        listaCont = [["","nan",""]]
    
    """['nome','numero','msg']"""
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager as cdm
    from time import sleep
    from selenium.webdriver.common.keys import Keys # biblioteca para aperta o enter 
    import urllib # tratar texto da url ex: texto = urllib.parse.quote(frase)
    from random import randint
    from geraLinks import links


    
    def espere(id_pg):
        """faz o navegador esparar até ser feita a leitura do qr code"""
        elementExist = 0
        while elementExist < 1:
            elementExist = len(browser.find_elements_by_id(id_pg))
            sleep(1)

    clica = lambda path : browser.find_element_by_xpath(path).click() # clica em campo

    enter = lambda enterPath : browser.find_element_by_xpath(enterPath).send_keys(Keys.ENTER)  

    def numsEx():
        from excel import excel
        nums = excel("tabela.xlsx")
        return[numero.split(',') for numero in nums]
    

    # navegar no whatsapp
    browser = webdriver.Chrome(cdm().install())
    browser.maximize_window()
    contat = listaCont
    #print(contat)
    for c in listaCont:
        for contato in range(len(links(c))):
            
            browser.get(links(c)[contato])
            espere("side")


            clica('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
            sleep(1)
            enter('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
            sleep(randint(3,10))

    clica('//*[@id="side"]/header/div[2]/div/span/div[3]/div')
    sleep(2)
    clica('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]/div[1]')
    sleep(2)
    browser.close()

if __name__ == "__main__":
    #botWhatsapp([['nan', '5556738920323,', 'Mensagem que será enviada pelo bot...'], ['nan', '5562326572383,', 'Mensagem que será enviada pelo bot...']])
    botWhatsapp([])