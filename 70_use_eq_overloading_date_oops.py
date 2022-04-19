class DateMonthYear:

    def __init__(self,d,m,y):
        self.__dt , self.__mth , self.__yr = d,m,y

    def __eq__(self,other):
        
        if self.__dt == other.__dt and self.__mth == other.__mth and self.__yr == other.__yr:
            return True
        
        else:
            return False

d1 = DateMonthYear(23 , 3 , 2004)
d2 = DateMonthYear(23 , 3 , 2004)
d3 = DateMonthYear(30 , 7 , 2004)

print(id(d1))
print(id(d2))

print(d1 == d3)