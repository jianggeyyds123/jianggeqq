
#利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter

string = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf"
words = string.split(";")  # 拆分字符串为单词列表

word_counts = Counter(words)

print(word_counts)
