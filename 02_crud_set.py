set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)


# add
set_countries.add('pe')
print(set_countries)
set_countries.add('pe') #no se agrega doble elemento
print(set_countries)

# update
set_countries.update({'ecua', 'arg', 'pe'})
print(set_countries)

# remove
set_countries.remove('col')
print(set_countries)

set_countries.remove('arg')
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

set_countries.clear()
print(set_countries)
print(len(set_countries))