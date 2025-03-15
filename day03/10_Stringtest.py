stringtest="Hello Python"
print(stringtest)
print(f"第四个字符串：{stringtest[4]}，倒数第二个字符串{stringtest[-2]}")

#stringtest[4]="P"
#这里字符串不允许修改 --只读的 需要重新创建新的字符串
#print(stringtest)
print(f"字符串ll的位置：{stringtest.index("ll")}")

print(f"替换字符串h为A：{stringtest.replace("o","A")}")
#原字符串本身不会变化 只是得到一个新的字符串 不信你输出一下
print(stringtest)
print(f"拆分字符串h为A：{stringtest.split(" ")}")

stringtestStrip01=" Hello Python "
#不传参 去除前后空格以及回车
print(f"去除前后空格以及回车后为：{stringtestStrip01.strip()}")
print(f"去除前后空格以及回车前字符串长度：{len(stringtestStrip01)}")
print(f"去除前后空格以及回车后字符串长度：{len(stringtestStrip01.strip())}")
stringtestStrip02="A1 Hello Python 1A"
#Strip中的参数会被拆分成两个字符串A 和1  分别匹配 满足其一即可
print(f"指定strip参数后为：{stringtestStrip02.strip("A1")}")

for elem in stringtestStrip02:
    print(elem)
