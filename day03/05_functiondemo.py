totalmoney=50000.00

def query_1():
    print("您选择了[查询余额]")
    print(f"您当前余额为{totalmoney}，祝您生活愉快")
    main_page()

def deposit_2():
    global totalmoney
    print(f"你选择了[存款]，您当前余额{totalmoney}")
    your_deposit = int(input("请输入存款金额:"))
    totalmoney=totalmoney+your_deposit
    print(f"[存款]成功，您当前余额{totalmoney}")
    main_page()

def width_draw_3():
    global totalmoney
    print(f"你选择了[取款]，您当前余额{totalmoney}")
    your_withdraw = int(input("请输入取款金额:"))
    if totalmoney - your_withdraw>=0:
        totalmoney = totalmoney - your_withdraw
        print(f"[取款]成功，您当前余额{totalmoney}")
    else:
        print(f"余额不足，当前余额[{totalmoney}]，取款金额[{your_withdraw}]")
    main_page()

def exit_4():
    print("你选择了[退出]，欢迎下次使用")
    main_page()

def main_page():
    print("***********************请选择菜单操作***********************\n")
    print("查询余额\t\t[输入1]")
    print("存款\t\t\t[输入2]")
    print("取款\t\t\t[输入3]")
    print("退出\t\t\t[输入4]")
    print("***********************请选择菜单操作***********************\n")
    your_selection = int(input("请输入您的选择:"))
    if your_selection == 1:
        query_1()
    elif your_selection==2:
        deposit_2()
    elif your_selection==3:
        width_draw_3()
    elif your_selection==4:
        exit_4()
    else:
        print(f"无效的选项[{your_selection}]")

def welcome():
    name=input("你好欢迎光临瑞士银行取款,请输入姓名\n")
    print("")
    print(f"欢迎您尊敬的客户\t{name},")



welcome()
main_page()