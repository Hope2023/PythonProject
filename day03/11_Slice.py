stringArray=[0,1,2,3,4,5,6,7,8,9,10]
print(stringArray[1:4])#步长为1可以不写
print(stringArray[1:4:2])#步长为2
print(stringArray[:])#步长为1
print(stringArray[::2])#步长为2

stringtuple=(1,2,3,4,5,6,7,8,9)
print(stringtuple[4:1:-1])#步长为-1
print(stringtuple[::-1])#步长为-1 翻转
print(stringtuple[::-2])#步长为-2

stringstr="Hello Python @2025"
print(stringstr[::-1][4:0:-1])#多次切片