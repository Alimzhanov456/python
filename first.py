
print("Здорова мня зовут Опера!!! ")
name = str(input('Как вас зовут? '))
age = int(input('Сколько вам лет? '))
wau = str(input('Где вы живете?'))
hobby = str(input('Какое у вас хобби? '))
email_ = str(input('Какой у вас email? '))
animal = str(input('У вас есть домашний питомец? '))
phone = str(input('Модель вашего телефона? '))
phone_num = int(input('Ваш телефон номер? ')) 
high = float(input('Какой ваш рост? '))
adress = str(input('Ваш домашний адресс? '))
print('-'*30)
print(f'Вас зовут - {name.capitalize()}\n'
      f'Вам полных - {age} лет\n'
      f'Вы живете - {wau} \n'
      f'Ваше хоби - {hobby}\n'
      f'Ваш email - {email_}\n'
      f'У вас есть - {animal}\n'
      f'Вы пользуйтесь - {phone}\n'
      f'У вас - {phone_num}\n'
      f'Рост - {high}\n'
      f'Вы живете - {adress}')
print('Спасибо!')

