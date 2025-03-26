import time

f=open("D:/Z004310X/New Text Document.txt","r",encoding="utf-8")
print(f"类型={type(f)}")
#读取100字节数据
# print(f.read(100))
#全部内容  多个read 在一起时 后面的read会跟着前面的read读完的位置继续读取
# print(f.read())

# print(f.readlines())

# for line in f:
#     print(line)

 #关闭文件 停止占用
f.close()




#with open 会自动关闭文件

with open("D:/Z004310X/New Text Document.txt","r",encoding="utf-8") as f:
    for line in f:
        print(line)