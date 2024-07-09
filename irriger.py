import pyautogui
import time
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
pyautogui.position(x=542, y=83)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('https://scheduling.valleyirrigation.com/home.php?area=decisao_gerenciar')
pyautogui.press('enter')
