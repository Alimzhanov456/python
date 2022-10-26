#day = int(input("введите день вашего рождения!"))
#month = int(input("введите месяц вашего рождения!"))
#if day>=21 and month == 3 or day <=20 and moth ==4:
 #   print('Вы овен')
#else:
 #   print('Вы не овен')


apple = 4
good_box = 0
bad_box = 0
while apple <4:
    a = input('какое яблоко? ')
if a == "bad":
    bad_box +=1
    apple<4
    print('в bad_box')
elif a == "good":
    good_box+=1
    print('в good_box')
apple-=1
print('все')