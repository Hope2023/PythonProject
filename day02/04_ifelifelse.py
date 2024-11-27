age=int(input("Enter your age: "))

if age>0:
    print(f"你的年纪是{age}")
    if age <= 7:
        print(f"学龄前儿童")
    elif  age <= 13:
        print(f"小学")
    elif age <= 16:
        print(f"初中")
    elif age <= 19:
        print(f"高中")
    elif age <= 23:
        print(f"大学")
    else:
        print(f"硕士及以上")
else:
    print(f"无效年纪")

