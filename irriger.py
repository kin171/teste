import pyautogui
import time
import tabula
import pandas as pd

pyautogui.PAUSE = 2

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://scheduling.valleyirrigation.com/index.php')
pyautogui.press('enter')
pyautogui.write('antonio.honorio@raizen.com')
pyautogui.press('tab')
pyautogui.write('honorio171')
#pyautogui.press('tab')
#pyautogui.press('enter')
pyautogui.click(x=905, y=742)
time.sleep(5)
pyautogui.click(x=1146, y=76)
pyautogui.click(x=34, y=142)
pyautogui.click(x=127, y=303)
pyautogui.click(x=135, y=362)
pyautogui.click(x=1862, y=233)
pyautogui.click(x=1414, y=778)
pyautogui.click(x=1795, y=140)
pyautogui.click(x=766, y=562)
#pyautogui.press('enter')
#dados = tabula.read_pdf('"C:\Users\kin50\Downloads\mpdf.pdf"')
