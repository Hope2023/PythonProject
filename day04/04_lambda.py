#定义匿名函数  只能调用一次 无法二次使用只能写一行
def test_func(compute):
    result = compute(1,2)
    print(result)
#定义匿名函数表示返回两个参数两项  可以比较03文件两种方式的差异
test_func(lambda num1,num2: num1+num2)