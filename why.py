from xmlrpc.client import Boolean


lesson = ("I", "L", "O", "V", "E", "P", "H", "O", "N", "E", 2,1,3,4,5,12,13,15,14.50,22.111, True, False)
word = []
nummer = []
boolean = []
for i in lesson:
    
    if type(i) == str:
        word.append(i)
    elif type(i) == int or type(i) == float:
        nummer.append(i)
    elif type(i) == bool:
        boolean.append(i)

word.reverse()
nummer.sort()
boolean.sort()

word = tuple(word)
nummer = tuple(nummer)
boolean = tuple(boolean)


print(word)
print(nummer)
print(boolean)
