try:
    f=open("D:/test.txt","r",encoding="utf-8")
except:
    print("error no such files, start creating")
    #w 模式会创建文件
    f=open("D:/test.txt","w",encoding="utf-8")


try:
     1/0
    #  print(name)
except(NameError,ZeroDivisionError) as e:
    print(e)


try:
    #Exception用于捕获所有异常
    1/0
except Exception as e:
    print(e)
else:
    print("没有异常的处理逻辑")
finally:
    print("肯定会执行的逻辑无论是否有异常 比如文件关闭")


def func1():
    print("func1 开始")
    1/0
    print("func1 结束")

def func2():
    print("func2 开始")
    func1()
    print("func2 结束")

def main():
    try:
        func2()
    except Exception as e:
        print(e)
main()