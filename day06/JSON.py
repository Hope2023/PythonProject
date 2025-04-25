import json
#列表转JSON
data=[{"name":"Allen","age":"30"},{"name":"Alex","age":"20"}]
print(json.dumps(data))

#字典转JSON
data2={"name":"Allen","age":"30"},{"name":"Alex","age":"20"}
print(json.dumps(data2))

#JSON str转JSON
data3='[{"name":"Allen","age":"30"},{"name":"Alex","age":"20"}]'
print(json.loads(data3))