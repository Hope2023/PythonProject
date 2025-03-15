#集合不支持下标索引 不能用while 循环
setStr={"Hello","hello","Python","Java","hello",11,5.5,True}
#无序 去重
print(setStr)
print(len(setStr))

setStr.add("Java")
print(setStr)

setStr.remove("Hello")
print(setStr)

#随机取
print(setStr.pop())

print(setStr.clear())


set1={1,2,3,4,5}
set2={2,4,6,8,10}
#差集
print(set2.difference(set1))
#set1中消除和set2相同的元素
set1.difference_update(set2)
print(set1)#变化
print(set2)#不变化
#并集
print(set1.union(set2))

for element in set1.union(set2):
    print(element,end="\t")