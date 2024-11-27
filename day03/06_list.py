name_list=["Allen","Alex","Adam"]
print( name_list)
print(type(name_list))

mixed_list=["Allen",6666,True]
print( mixed_list)
print(type(mixed_list))


name_list=[["Allen","Alex","Adam"],["Black","Bill","Brain"]]
print(name_list)
print(len(name_list))
print(type(name_list))


print(name_list[0])

print(mixed_list.index("Allen"))

for i in name_list:
    for j in i:
        print(j)


mixed_list[0]="Amber"
print(mixed_list)
mixed_list.insert(3,"Allen")
print(mixed_list)

# 追加单个
mixed_list.append("Tmep")
print(mixed_list)


# 追加list
extended_list=[["Check","Cow"]]
name_list.extend(extended_list)
print(name_list)


del name_list[2]
print(name_list)

mylist=[1,2,3,4,5]
element=mylist.pop(2)
print(mylist,element)



# 从前到后删除只删除一次
mylist=[1,2,3,4,5]
element=mylist.pop(2)
print(mylist.remove(2))

mylist=[1,2,3,4,5]
mylist.clear()
print(mylist)
print(mylist.count())