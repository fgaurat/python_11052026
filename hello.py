print("Bonjour")

# Les types de données
a = 1
print(a)
print(type(a))

t = "Hello"
t = 'Hello'
print(t)
print(type(t))

t1 = "1"
print(t1)
print(type(t1))

b=1.2
print(b)
print(type(b))

c = False
print(c)
print(type(c))

# s = 'L\'orage gronde'
s = "L'orage gronde"
print(s)

# p = "c:\\newproject\\test1"
p = r"c:\newproject\test1"
print(p)

lines = """ligne1
ligne2
ligne3
ligne4
"""
print(lines)

a= 1
s = "la valeur de a:"+str(a) # cast ou transtypage de a en string
print(s)


print("-"*50)
a = 3
s = "toto"*3
print(s)

print("-"*50)

p = "Bonjour"
print(p[0]) # B
print(len(p))
print(p[len(p)-1])
print(p[-1])

print(p[1:4]) # onj => le dernier élément d'un slice n'est pas inclus, en mathématique [1,4[

print(p[:3]) # Bon
print(p[3:]) # jour

print("-"*50)

a, b = 0, 1
while a < 10:
    print(a) # 0,1
    a, b = b, a+b # a,b = 1,2