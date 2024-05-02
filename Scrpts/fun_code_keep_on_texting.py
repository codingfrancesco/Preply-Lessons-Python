import pyautogui
import time




time.sleep(5)

for i in range(1,100):
    pyautogui.write(f' hello {i+1} ', interval=0.1)  # Type with quarter-second pause in between each key.
    pyautogui.press('enter') 


