#字典不支持下标索引 不支持while循环
dict_str={"Allen":99,"Simon":100,"Tom":89,"Jacky":"77"}
print(dict_str)

#空字典
dict2={}
dict3=dict()

#新值取代老值
dict_str4={"Allen":99,"Simon":100,"Tom":89,"Jacky":"77","Allen":66}
print(dict_str4)

score=dict_str4["Allen"]
print(f"Allen的分数是{score}")

dict_str5={
    "Allen":{"语文":88,"数学":99,"英语":80},
    "Simon":{"语文":80,"数学":90,"英语":88},
    "Tom":{"语文":85,"数学":89,"英语":78}
}
print(dict_str5["Allen"])
print(dict_str5["Allen"]["语文"])

#key 不可以为字典类型 value 任意  key不支持下标索引

dict_str2={"Allen":99,"Simon":100,"Tom":89,"Jacky":"77"}
dict_str2["Frank"]=90
print(dict_str2)

dict_str2["Allen"]=86
print(dict_str2)

#移除Tom
score=dict_str2.pop("Tom")
print(score)

#获取所有key
print(dict_str2.keys())

#直接循环key
for ele in dict_str2.keys():
    print(f"{ele}={dict_str2[ele]}",end="\t")

#每次循环都是抓到可以
for element in dict_str2:
    print(f"字典长度={len(element)}")
    print(f"key={element}",end="\t")
    print(f"value={dict_str2[element]}", end="\t")
