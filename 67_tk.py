import pywhatkit 
import time 

lc = time.time()
cur = time.ctime(lc)
print(cur)

lc2 = lc+30
cur2 = time.ctime(lc2)
print(lc2)
print(cur2)


pywhatkit.sendwhatmsg("+918799229044" , "good night" ,cur2)
