#passo 1 enrar no sistema empresa
#passo 2 fazer login
#passo 3 cadastra produtos
import pyautogui
import time
#pyautogui.click
#pyautogui.write
#pyatogui.press
#pyautogui.hotkey
#pyautogui.scroll
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)
pyautogui.position(x= 805, y = 467)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('tab')
pyautogui.write('kin5090@hotmail.com')
pyautogui.press('tab')
pyautogui.write('logan171')
pyautogui.press('tab')
pyautogui.press('enter')
import pandas
tabela = pandas.read_csv('produtos.csv')
print (tabela)


for linha in tabela.index:
    pyautogui.click(x = 839, y = 321 )
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    
    marca = str(tabela.loc[linha,'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    
    pyautogui.press('tab')
    pyautogui.press('enter')    
    6.5     
    pyautogui.scroll(5000)
