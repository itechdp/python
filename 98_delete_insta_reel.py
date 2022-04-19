from time import sleep 
import pyautogui as pg


sleep(5.00)
pg.press('tab',2)
pg.press('enter')                                                                                                                                                                                                                                           
pg.write('chrome')
pg.press('enter')
sleep(30.00)
pg.write('instagram.com/i.techdp/reels/')
sleep(10.00)

for i in range(50):
    sleep(15.00)
    pg.press('tab',60)
    pg.press('enter')
    sleep(5.00)
    pg.press('tab',9)
    pg.press('enter')
    sleep(3.00)
    pg.press('tab')
    pg.press('enter')
    sleep(3.00)   
    pg.press('tab')
    pg.press('enter')        
    sleep(10.00)                                                                                                                                                                                                                            
    pg.hotkey('ctrl','r')
        