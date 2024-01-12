import pandas as pd
import pyautogui
import time 

#Passo a passo do projeto 

#time.sleep(0.5) 

#PASSO 1: Entrar no sistema da empresa
#aperto command + space, digito google, escrevo o link e  aperto enter.

#entrar no navegador
pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")
time.sleep(1)
pyautogui.write("safari")
pyautogui.press("enter")
time.sleep(1)

#entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")    
pyautogui.press("enter")
time.sleep(3)


#PASSO 2:  clicar no campo email, escrever o email, dar um tab, escrever a senha, pressionar enter.

pyautogui.PAUSE = 0.3
pyautogui.click(x=533, y=372)#clicando no campo email
pyautogui.write("aprendendo_python_automatacao@gmail.com") #escrevendo o email
pyautogui.press("tab")
pyautogui.write("senhadopython")
pyautogui.press("enter")

#PASSO 3: Ler o banco de dados que importamos no inicio do código

tabela = pd.read_csv("produtos.csv")
print(tabela)

#PASSO 4: Cadastrar os produtos:
#clicar no campo do codigo do produto, acessa o banco de dados, pega o codigo e digitar. Depois dar tab e fazer a mesma coisapara os demais campos.


for linha in tabela.index:
    # Clicar no campo de código
    pyautogui.click(x=406, y=249)
    pyautogui.PAUSE = 0.3
    colunas = ["codigo","marca", "tipo", "categoria", "preco_unitario", "custo"]
    for coluna in colunas:
        pyautogui.write(str(tabela.loc[linha, coluna]))
        pyautogui.press("tab")
        time.sleep(0.5)
    
    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    
    # pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.scroll(1000)




