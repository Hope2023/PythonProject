import random
money=10000

for i in range(1,21):
    score=random.randint(1,10)
    if score<5:
        print(f"员工{i}，绩效分{score}，不满足绩效，不发工资")
        continue
    if money>=1000:
        money-=1000
        print(f"员工{i}，绩效分{score}，发工资1000，剩余{money}")
    else:
        print("余额不足")

