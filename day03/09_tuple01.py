# 元祖不可修改
tuple01 = (1, 'Hello', True)
tuple02 = ()
tuple03 = tuple()
print(type(tuple01))
print(tuple01)
print(type(tuple02))
print(tuple02)
print(type(tuple03))
print(tuple03)
print(f"Hello的数量：{tuple01.count("Hello")}")

# 单个元素需要逗号
tuple02 = (1)
print(type(tuple02))
print(tuple02)

tuple03 = (1,)
print(type(tuple03))
print(tuple03)
print((tuple03.index(1)))
print(tuple03.count(1))

tuple04 = ((1, 2, 3), (4, 5, 6))
print(f"t04的是类型是:{type(tuple04)}")
print(tuple04[1][2])
print(len(tuple04))

tuple05 = ((1, 2, 3), (4, 5, 6), ["Hello"])
# 元祖中元素不可修改 除非嵌套了其他类型如 list 数组等
tuple05[2][0] = "Hi"
print(tuple05)


print(tuple05.count("Hello"))
print(tuple05.count("Hi"))
print(len(tuple05))


for element in tuple05:
    print(f"元素有：{element}")