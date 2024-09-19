# 表达式
print("1*1=%d"%(1*1))
print(f"1*1={1*1}")

name="Siemens"
stock_price=165.5
stock_code="Siemens AG"
growth_factor=1.01
growth_days=10

print(f"公司名称：{name},股票代码：{stock_code},当前股价:{stock_price}")
stock_price=stock_price*growth_factor**growth_days
print("每天增长系数：%.2f，经过:%d天增长，股价为:%.2f"%(growth_factor,growth_days,stock_price))