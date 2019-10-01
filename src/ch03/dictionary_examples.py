person = {
    'name': 'Ford Prefect',
    'gender': 'male',
    'home planet': 'Betelgeuse Seven',
    'occupation': 'researcher'
}

person['age'] = 33

print(person)
print(person['name'])

fruits = {}
fruits['apples'] = 10
b =  'apples' in fruits
print(b)

for i in range(10):
    if 'banana' not in fruits:
        fruits['banana'] = 0
    else:
        fruits['banana'] += 1
print(fruits)

fruits.setdefault('pear', 0)
fruits['pear'] += 2
fruits.setdefault('pear', 0)
print(fruits)