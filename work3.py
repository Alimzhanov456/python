#3
class Book:
    def __init__(self, title,year, color):
        self.title = title
        self.year = year
        self.color = color

    def __str__(self):
        return f'{self.title}\n' \
               f'{self.year}\n' \
               f'{self.color}'


class Childrensbook(Book):
    def __init__(self, title, year, color):
        super().__init__(title, year, color)

    def __str__(self):
        return super(Childrensbook, self).__str__()

class Romanticbook(Book):
    def __init__(self, title, year, color):
        super().__init__(title, year, color)
    def __str__(self):
        return super(Romanticbook, self).__str__()

class Teenbook(Childrensbook, Romanticbook):
    def __init__(self, title, year, color):
         super().__init__(title, year, color)
    def __str__(self):
      return super(Teenbook,self).__str__()

b = Book(title="all", year="all", color="all")
c = Childrensbook(title="Сказки", year="от 3 лет",color="rainbow")
r = Romanticbook(title="Про любовь", year="от 25 лет", color="red,black,pink")
t = Teenbook(title="Для подростков", year="от 16 лет", color="light color")

print(b)
print(c)
print(r)
print(t)
print("-"*20)
