# num=1024
#
# if int(input("猜猜看啊"))==num:
#     print("Awesome, 猜对了")
# elif int(input("猜错了，再来一次"))==num:
#     print("Awesome, 猜对了")
# elif int(input("最后一次机会")) == num:
#     print("Awesome, 猜对了")
# else:
#     print("Out")

num = 1024
if int(input("猜猜看啊")) == num:
    print("Awesome, 猜对了")
else:
   if int(input("很接近了"))>=1000:
       print("很接近了")
       if int(input("再努力一下")) >= 1020:
           print("十分接近")
       else:
           print("太可惜了")
   else:
       print("差的有点远")