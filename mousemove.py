import pyautogui
import time

while True:
    pyautogui.moveRel(1, 0, duration=1)
    pyautogui.moveRel(-1, 0, duration=1)
    time.sleep(60)
