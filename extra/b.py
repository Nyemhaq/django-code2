import pyautogui

n = int(input())

for i in range(0,n+1):
    pyautogui.write('*' * i, interval=0.25)  
    pyautogui.press('enter')

