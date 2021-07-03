l = ['Bob', 'Rolf', 'Anne']
t = ('Bob', 'Rolf', 'Anne')
s = {'Bob', 'Rolf', 'Anne'}

print(l[0])
print(t[0])
print(s)

l[0] = 'Smith'
print(l)

l.append('Bob')
print(l)

# t[0] = 'Smith'
# print(t)

# t.append('Smith')
# print(t)

s.add('Smith')
print(s)