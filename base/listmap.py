a = [1,2,3]

a.insert(1,9)
print(a)
print(a.index(9))

a.reverse()
print(a)

a.sort()
print(a)

a.pop()
print(a)

a.remove(3)
print(a)

a.append(99)
print(a)




####集合
st = {'aa','ab','ad','bb'}
print('aa' in st)
print('cc' in st)


#####map
map = {'key1':'va1', 'key9':'va9', 'key3':'va3'}
print(map['key3'])
print(map.get('key9'))
map['key6'] = 'va6'
print(map)
print(list(map.keys()))
print(sorted(map.keys()))

for k, v in map.items():
    print(k, v)
for k, v in sorted(map.items()):
    print(k, v)