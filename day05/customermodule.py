__all__=["test"]  #当其他python文件通过导包方式用*调用本文件时 只会导入test方法

def test(a,b):
    print(a+b)

def testMin(a, b):
    print(a - b)


#内置变量 main 可以在当前python中单独运行test，同时在调用当前python的的文件中不执行test
if __name__ == '__main__':
    test(1,2)

