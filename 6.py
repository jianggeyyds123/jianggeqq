#如何在一个函数内部修改全局变量
#利用global在函数声明修改全局变量
count = 0  # 全局变量

def increment():
    global count  # 使用 global 声明 count 是全局变量
    count += 1

increment()
print(count)  # 输出结果为 1