import time
import pyautogui

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.click(x=775, y=292)
pyautogui.write("vcs e mt ff")
pyautogui.press("enter")