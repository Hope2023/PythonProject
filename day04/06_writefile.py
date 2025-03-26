

# f=open("D:/Z004310X/New Text Document.txt","w",encoding="utf-8")
# #写入内存 不存在则创建  覆盖原内容
# f.write("Hello python")
# #写入硬盘
# # f.flush()
# #close 带flush功能
# f.close()


#不会清空 只会追加
f1=open("D:/Z004310X/New Text Document.txt","a",encoding="utf-8")
f1.write("Hello python\n")


#close 带flush功能
f1.close()




