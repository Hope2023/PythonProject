# 字符串 单引号 双引号 三引号
print('AllenWalker')
print("AllenWalker")
print("""AllenWalker""")

print('"AllenWalker"')
print("'AllenWalker'")
print("\'AllenWalker\'")
print("\"AllenWalker\"")


print("Allen" + " Walker")
name="Allen Walker"
age=20
print("name=" + name+ " , age=" + str(age))

message="name=%s,age=%s"%(name,age)
print(message)

height=175.5
message="name=%s,age=%d,height=%f"%(name,age,height)
print(message)


message="name=%s,age=%d"%(name,age)
print(message)

height=175.5
message="name=%s,age=%3d,height=%4.1f"%(name,age,height)
print(message)

height=175.5
# 只限制小数不限制长度
message="name=%s,age=%3d,height=%.1f"%(name,age,height)
print(message)

# 优雅的方式 快速格式化  不限数据类型 不做精度控制
print(f"name={name},age={age+10},height={height}")
