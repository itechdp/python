class Addition:
    def addi(self):
        return self.a + self.b

    @staticmethod
    def greet():
        print("hello dhrumil!!!")


num = Addition()

num.a = 10
num.b = 20

s = num.addi()
print(s)

num.greet()
