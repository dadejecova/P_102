set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# union
set_c = set_a.union(set_b)
print(set_c)

print(set_a | set_b)

# intersección
set_c2 = set_a.intersection(set_b)
print(set_c2)
print(set_a & set_b)

# diferencia
set_c3 = set_a.difference(set_b)
print(set_c3)
print(set_a - set_b)

# diferencia simetrica
set_c4 = set_a.symmetric_difference(set_b)
print(set_c4)
print(set_a ^ set_b)