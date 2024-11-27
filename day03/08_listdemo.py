number=[1,2,3,4,5,6,7,8,9,10]
odd=[]
for i in number:
    if(i%2==0):
        odd.append(i)
print(odd)

number_2=[1,2,3,4,5,6,7,8,9,10]
j=0
odd_2=[]
while j< len(number_2):
    if (number_2[j] % 2 == 0):
        odd_2.append(number_2[j])
    j+=1
print(odd_2)
