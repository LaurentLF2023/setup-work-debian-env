import pyautogui
import time
import pyperclip
import os

directory = "cd epitech/projets/semestre2/free_ads/W-PHP-502-NAN-2-1-FreeAds-laurent.le-foulgoc/freeads"
server = 'php artisan serve'
sql = 'sudo service mariadb start'

pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('terminal')
pyautogui.press('enter')
time.sleep(2)

pyperclip.copy(directory)
time.sleep(0.5)
pyautogui.hotkey('ctrl','v')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write(server)
pyautogui.press('enter')
time.sleep(2)

pyautogui.hotkey('alt','shift','6')
time.sleep(0.7)
pyautogui.write(sql)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write(os.environ['PWD'])
pyautogui.press('enter')
time.sleep(0.7)

pyautogui.hotkey('alt','shift','6')
time.sleep(1)
pyperclip.copy(directory)
pyautogui.hotkey('ctrl','v')
time.sleep(0.3)
pyautogui.press('enter')
time.sleep(0.5)

pyautogui.hotkey('alt','shift','6')
time.sleep(1)
pyperclip.copy(directory)
pyautogui.hotkey('ctrl','v')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.write('code .')
time.sleep(0.3)
pyautogui.press('enter')