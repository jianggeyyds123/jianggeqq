#字典根据键从小到大排序
dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}

sorted_dict = dict(sorted(dic.items(), key=lambda x: x[0]))

print(sorted_dict)
