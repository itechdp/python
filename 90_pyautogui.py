from time import sleep
import pyautogui as pg 

sleep(5.00)

for i in range(1,101):
    pg.write(f"Sorry Darling {i}")
    pg.press('enter')