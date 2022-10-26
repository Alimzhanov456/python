sport_cars = []
modern_cars = []
old_cars = []
european_cars = []
asian_cars = []
american_cars = []
russian_cars = []


cars = [
    {'title': 'BMW', 'Country':'Germany', 'volume': 3.0, 'type': 'sport'},
    {'title': 'Daewo', 'Country':'Uzbekiston', 'volume':1.8, 'type': 'old'},
    {'title': 'Tesla', 'Country':'American', 'volume': 3.0, 'type': 'modern'},
    {'title': 'Toyota', 'Country':'Japan', 'volume': 2.9, 'type': 'modern'},
    {'title': 'Ferrari', 'Country':'Italy', 'volume': 3.2, 'type': 'sport'},
    {'title': 'Mustang', 'Country':'American', 'volume': 3.0, 'type': 'sport'},
    {'title': 'Lambborghini', 'Country':'Italy', 'volume': 3.3, 'type': 'sport'},
    {'title': 'Bentley', 'Country':'England', 'volume': 2.8, 'type': 'modern'},
    {'title': 'Porsche', 'Country':'Germany', 'volume': 3.0, 'type': 'sport'}
]

europe = ['Germany','Italy','Sweden','England']
asia = ['Korea','Japan']
russia = ['Russia','Uzbekiston']
america = ['America']


def filter_type(cars):
    for i in cars:
        if i['type'] == 'sport':
            sport_cars.append(i)
        elif i['type'] == 'modern':
            modern_cars.append(i)
        elif i['type'] == 'old':
            old_cars.append(i)
    

def filter_country(cars):
    for i in cars:
        if i['Country'] in europe:
            european_cars.append(i)
        elif i['Country'] in asia:
            asian_cars.append(i)
        elif i['Country'] in america:
            american_cars.append(i)
        elif i['Country'] in russia:
            russian_cars.append(i)


filter_country(cars)
print(f'european_cars - {european_cars}')
print(' - ' *30)

filter_country(cars)
print(f'asian_cars - {asian_cars}')
print(' - ' *30)

filter_type(cars)
print(f'modern_cars - {modern_cars}')
print(' - ' *30)

filter_type(cars)
print(f'sport_cars - {sport_cars}')