# 循环100次
# i=0
# while i<100:
#     print(f"i={i}")
#     i+=1


# 1-100 求和
# i = 1
# total = 0
# while i < 101:
#     total += i
#     i += 1
# print("total=",total)


import random
num=random.randint(1,100)
i=0
flag=True
while flag:
    input_num = int(input("Enter a number: "))
    i+=1
    if input_num == num:
        print("Correct!")
        flag=False
    else:
        if input_num > num:
            print("To high")
        else:
            print("To low")
print(f"总共猜测了{i}次")