days=1
while days<=100:
    print(f"今天是第{days}天表白")
    flower=1
    while flower<=10:
        print(f"第{flower}朵玫瑰")
        flower+=1
    days+=1
print(f"第{days-1}天表白成功")


# 输出不换行
print("Hello ",end='')
print("World")

print("Hello\tWorld")

i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{i}*{j}={i * j}\t",end='')
        j+=1
    i+=1
    print("")
