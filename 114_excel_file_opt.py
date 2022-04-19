import pandas as pd

data = pd.read_excel(r'C:\Users\DHRUMIL PATEL\Desktop\dphotos.xlsx')
df = pd.DataFrame(data , columns=['mom'])
print(df)