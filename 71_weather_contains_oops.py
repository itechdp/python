class Weather:
    def __init__(self):
        self.__para = ['temprature', 'humidity']

    def __contains__(self,p):
        return True if p in self.__para else False
        
w = Weather()

if 'humidity' in w:
    print("valid weather")

else:
    print("invalid weather")