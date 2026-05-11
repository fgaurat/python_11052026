

a = 3

if a<3:
    print("a is less than 3")
    print(  "a is less than 3")
elif a==3:
    print("a is equal to 3")
else:    
    print("a is greater than 3")


if True:
    print("This is true")
    print("This is not false")

print("la suite")


l = ["valeur 1", "valeur 2", "valeur 3", "valeur 4", "valeur 5"]

print(l[0])


for value in l:
    print(value)


for i in range(len(l)):
    print(i,l[i])


# 0
# 1
# 2
# 3
# 4



# break
for i in range(10):
    if(i>5):
        break
    print(i)
print("-"*50)

for i in range(10):
    if(i%2==0):
        continue
    print(i)


print("-"*50)
# break
to_find = 79
found = False
for i in range(10):
    if(i==to_find):
        found = True
        break
    print("parcours",i)
else:
    print("parcours terminé sans trouver",to_find)


# if found:
#     print(to_find," is found")
# else:    
#     print(to_find," is not found")

print("-"*50)    


if False:
    pass
        

print("This is false")