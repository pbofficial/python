friends_a = {'Joey', 'Rachel'}
friends_b = {'Ross', 'Chandler'}

print(friends_a.union(friends_b))
print(friends_a.intersection(friends_b))

friends_a.add('Ross')
friends_a.add('Pheobe')

print(friends_a.intersection(friends_b))
print(friends_a.difference(friends_b))
print(friends_b.difference(friends_a))

print(friends_a.symmetric_difference(friends_b))