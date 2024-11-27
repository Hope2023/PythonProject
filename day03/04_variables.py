
# 全局变量无法在函数体内部修改，除非声明为global

num = 100

def test1():
    print(f"num={num}")

def test2():
    global num 
    num=120
    print(f"num={num}")

test1()
test2()