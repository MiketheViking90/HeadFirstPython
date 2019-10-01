import pprint

people = {}
people['Ford'] = {
    'name' : 'Ford Prefect',
    'gender' : 'male',
    'occupation': 'researcher',
    'planet' : 'Betelgeuse Seven'
}
pprint.pprint(people)
print(people['Ford']['occupation'])