#1
class movie:
    def __init__(self,hobby):
        self.hobby = hobby

    def interest(self):
        return f"Он смотрит фильмы, потому что любит {self.hobby}"

class series:
    def __init__(self,hobby):
        self.hobby = hobby

    def interest(self):
        return f"Он смотрит сериалы, потому что любит {self.hobby}"

class Book:
    def __init__(self,hobby):
        self.hobby = hobby

    def interest(self):
        return f"Он книжный червь, потому что любит {self.hobby}"

anime = Anime('фильм,например Титаник')
dorama = Dorama('сериалы,например Игра престолов ')
book = Book('книги, например Тихий Дон')

print(anime.interest())
print(dorama.interest())
print(book.interest())
