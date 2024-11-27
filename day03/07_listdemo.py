from operator import index

age=[21,25,21,23,22,20]

age.append(31)
print(age)

new_age=[29,33,30]
age.extend(new_age)
print(age)

print(age[0])
print(age[len(age)-1])
print(age[-1])

print(age.index(31))

for i in age:
    print(f"{i}\t",end="")

print("")
i=0
while i<len(age):
    print(f"{i}\t",end="")
    i+=1



