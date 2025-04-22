import time
# 导入time.py包
print("Hello")
time.sleep(5)
print("Python")

from time import  sleep  #只导入time中的sleep方法
print("Hello")
sleep(5) #直接使用sleep
print("Python")


from time import  *
print("Hello")
sleep(5) #直接使用sleep
print("Python")

from time import  sleep  as s#只导入time中的sleep方法 并起别名S
print("Hello")
s(5) #直接使用sleep
print("Python")


#导入自定义模块
import customermodule
customermodule.test(1,2)

