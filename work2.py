#2
class Instagram:
    def __init__(self, nikname, email, password):
        self.nikname = nikname
        self.email = email
        self.__password = password

    def __str__(self):
        return f'nikname - {self.nikname}\n'\
               f'email - {self.email}\n'\
               #f'password - {self.password}'

inst = Instagram(nikname="Alimzhanov", email="AlimzhanovErbol.com", password="123234345")
print('-'*20)
print(inst)
print('-'*20)
