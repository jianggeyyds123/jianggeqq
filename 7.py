
#字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"
import re

a = "not 404 found 张三 99 深圳"

filtered_text = re.sub(r'\b[a-zA-Z0-9]+\b', '', a)

final_output = ' '.join(filtered_text.split())

print(final_output)
