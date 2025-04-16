import pyautogui
import time

def chicken_wing():
    while True:
        pyautogui.keyDown("w")
        time.sleep(0.0000000000000000000000000001)
        pyautogui.keyUp("w")
    
        pyautogui.keyDown("a")
        time.sleep(0.0000000000000000000000000001)
        pyautogui.keyUp("a")
    
        pyautogui.keyDown("s")
        time.sleep(0.0000000000000000000000000001)
        pyautogui.keyUp("s")
    
        pyautogui.keyDown("d")
        time.sleep(0.0000000000000000000000000001)
        pyautogui.keyUp("d")
