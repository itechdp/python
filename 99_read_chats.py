import pyautogui as pg
from time import sleep

sleep(10.00)

while True:
    pg.press('up',200)
    sleep(5.00)
    pg.press('down',10)
    sleep(5.00)