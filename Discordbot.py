import time
import pyautogui
from random import randint



j = 0
time.sleep(2)

while j <= 20:

    temps = randint(1,10)
    time.sleep(temps)

    pyautogui.press('capslock')
    pyautogui.typewrite('!', interval=0.2)
    pyautogui.press('capslock')

    temps = randint(2, 10)
    time.sleep(temps)

    pyautogui.typewrite('d bump', interval=0.3)
    pyautogui.press('enter')

    print("saisi effectué")

    temps = randint(2, 20)
    time.sleep(7200+temps)