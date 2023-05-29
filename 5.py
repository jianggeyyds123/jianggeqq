#python实现列表去重的方法
#先通过集合去重，在转列表
my_list = [1,2,2,3,4,4,5]
unique_set = set(my_list)
unique_list = list(unique_set)
print(unique_list)
