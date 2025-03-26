my_list=[1,2,3,4,5,6]
my_tuple=(1,2,3,4,5,6)
my_string="abcdefg"
my_set={1,2,3,4,5}
my_dict={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}

print(f"列表元素一共：{len(my_list)}")
print(f"元祖元素一共：{len(my_tuple)}")
print(f"字符串元素一共：{len(my_string)}")
print(f"集合元素一共：{len(my_set)}")
print(f"字典元素一共：{len(my_dict)}")

print(f"列表元素最大：{max(my_list)}")
print(f"元祖元素最大：{max(my_tuple)}")
print(f"字符串元素最大：{max(my_string)}")
print(f"集合元素最大：{max(my_set)}")
print(f"字典元素最大：{max(my_dict)}")

print(f"列表元素最小：{min(my_list)}")
print(f"元祖元素最小：{min(my_tuple)}")
print(f"字符串元素最小：{min(my_string)}")
print(f"集合元素最小：{min(my_set)}")
print(f"字典元素最小：{min(my_dict)}")

print(f"列表转列表：{list(my_list)}")
print(f"元祖转列表：{list(my_tuple)}")
print(f"字符串转列表：{list(my_string)}")
print(f"集合转列表：{list(my_set)}")
print(f"字典转列表：{list(my_dict)}")

print(f"列表转元祖：{tuple(my_list)}")
print(f"元祖转元祖：{tuple(my_tuple)}")
print(f"字符串转元祖：{tuple(my_string)}")
print(f"集合转元祖：{tuple(my_set)}")
print(f"字典转元祖：{tuple(my_dict)}")

#会自动去除双引号 实际上字符串类型
print(f"列表转字符串：{str(my_list)}")
print(f"元祖转字符串：{str(my_tuple)}")
print(f"字符串转字符串：{str(my_string)}")
print(f"集合转字符串：{str(my_set)}")
print(f"字典转字符串：{str(my_dict)}")

print(f"列表转集合：{set(my_list)}")
print(f"元祖转集合：{set(my_tuple)}")
print(f"字符串转集合：{set(my_string)}")
print(f"集合转集合：{set(my_set)}")
print(f"字典转集合：{set(my_dict)}")


my_list=[3,4,1,2,6,5]
my_tuple=(3,4,1,2,6,5)
my_string="cabfdeg"
my_set={1,2,3,4,5}
my_dict={"key3":3,"key4":4,"key1":1,"key2":2,"key5":5}
#全部转换为集合list
print(f"列表正向排序：{sorted(my_list)}")
print(f"元祖正向排序：{sorted(my_tuple)}")
print(f"字符串正向排序：{sorted(my_string)}")
print(f"集合正向排序：{sorted(my_set)}")
print(f"字典正向排序：{sorted(my_dict)}")

print(f"列表反向排序：{sorted(my_list,reverse=True)}")
print(f"元祖反向排序：{sorted(my_tuple,reverse=True)}")
print(f"字符串反向排序：{sorted(my_string,reverse=True)}")
print(f"集合反向排序：{sorted(my_set,reverse=True)}")
print(f"字典反向排序：{sorted(my_dict,reverse=True)}")

