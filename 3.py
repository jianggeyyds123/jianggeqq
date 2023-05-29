#字典如何删除键和合并两个字典
#del和update方法
my_dict = {'a': 1,'b': 2, 'c': 3}
del my_dict[ 'a']
print(my_dict)
dict1 = {'a':1,'b':2}
dict2 = {'c': 3, 'd ' : 4}
dict1.update(dict2)
print(dict1)