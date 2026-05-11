from collections import deque

l = [10,20,30,40,50]
l.append(60)
print(l)
last_value = l.pop()
print(l)
print(last_value)
first_value = l.pop(0)
print(l)
print(last_value)

l.insert(0, -10)
print(l)

d = deque(l)
print(d)
d.appendleft(-20)
print(d)

print("-" * 50)




b=1

# for i in range(100):
#     a.append(i)
# print(a)

# a =list(map(lambda x: x, range(100)))

# a =list(map(int, range(100)))

# Liste comprehension
a =[i for i in range(100)]
print(a)




print("-" * 50)
# list
# l = [10,20,30,40,50]

# tuple
t = 10,20,30,40,50
print(t)
# TypeError: 'tuple' object does not support item assignment
# t[0] = 1000
a,b=0,1


print("-" * 50)

s = {1,2,3,4,5}
print(s)
s.add(6)
print(s)
s.add(1)
print(s)
l = [10,20,30,40,50,20,30,40]
s = set(l)
l2 = list(s)
print(l2)

s1 = {1,2,3,4,5}
s2 = {-10,0,1,2,3}
s3 = s2-s1
print(s3)

print(50 * "-")

d1 = {"name":"Fred", "age":49, "city":"Sainte Geneviève des Bois"}

print(d1['name'])

d1['job']="dev"
print(d1)

for key in d1:
    print(key,  d1[key])

keys = d1.keys()
print(keys)
values = d1.values()
print(values)
items = d1.items()
print(items)
item0 = list(items)[0]
k,v = item0
print(k,v)
print()
for k,v in d1.items():
    print(k,v)

s1 = {1,2,3,4,5}

for i in s1:
    print(i)

l = [10,20,30,40,50]

for i,v in enumerate(l):
    print(i,v)