#4
class Manga:
    def __init__(self, title, year,genr ):
        self.title = title
        self.year = year
        self.genr = genr


    def __str__(self):
        return f'{self.title}\n' \
               f'{self.year}\n' \
               f'{self.genr}'

    def read(self):
        return f'it can be good for girl and boy'

class Anime1(Manga):
    def __init__(self, title,year, genr):
        super().__init__(title, year, genr)
    def __str__(self):
        return super(Anime1, self).__str__()

anime_1 = Anime1(title='Naruto', year=2005, genr="Senen")
print(anime_1.read())
print(anime_1)

class Film(Manga):
    def __init__(self,title,year, genr):
        super().__init__(title,year,genr)
    def __str__(self):
        return super(Film, self).__str__()

film1 = Film(title='Naruto shipyden', year=2012, genr="fantasy")
print(film1)
print(film1.read())