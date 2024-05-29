#Passo 1: Abrir o navegador para entrar no sistema 
#Passo 2: Fazer o login no sistema
#Passo 3: Importar a base de alunos
#Passo 4: Cadastrar os alunos

import pyautogui
import pandas as pd 
import time

tabela = pd.read_csv("alunos.csv")

pyautogui.PAUSE = 0.5

#Passo 1: Abrir o navegador para entrar no sistema 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")

#Passo 2: Fazer o login no sistema
pyautogui.click(x=2505, y=298)
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")

#Passo 3: Importar a base de alunos
tabela = pd.read_csv("alunos.csv")
time.sleep(3)

#Passo 4: Cadastrar os alunos

for linha in tabela.index:
    nome = tabela.loc[linha,"Nome"]
    email = tabela.loc[linha,"Email"]
    endereco = tabela.loc[linha,"Endereco"]
    telefone = tabela.loc[linha,"Telefone"]
    pyautogui.click(x=2415,y=399)
    pyautogui.write(str(nome))
    pyautogui.press("tab")
    pyautogui.write(str(email))
    pyautogui.press("tab")
    pyautogui.write(str(endereco))
    pyautogui.press("tab")
    pyautogui.write(str(telefone))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    

    
    
    

 

 