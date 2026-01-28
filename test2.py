import random
input_sentence = input("")
#以空格为分割，对字符串进行处理，使它输出为一个列表
input_list = input_sentence.split()

#下标索引相当于单词的“身份证”，想要对打乱后的句子本身进行还原（而不是依靠原文还原），必须要在打乱时也带着单词的索引
#这里的做法是：在大列表内部建立一个个小列表，每个列表存储单词和对应的下标；带着下标一起打乱后，取得一个带着下标的嵌套列表，再从中提取仅含单词的列表
#用map比较麻烦：以单词为key时，要考虑是否重复的问题；以索引为key时，不好赋值
original_list = []
for i in range (len(input_list)):
    word = input_list[i]
    original_list.append([i,word])

#带上索引，对input句子进行打乱
random.shuffle(original_list)
#去掉索引：element是大列表的元素，相当于一个个名字为element，由[索引，单词]组成的小列表，所以取得下标为1的元素就能取得单词
scrambled_list = []
for element in original_list:
    scrambled_list.append(element[1])
output_str=" ".join(scrambled_list)
print(f"scrambled outcome:{output_str}")

#根据打乱后的句子，对句子进行还原: 先排序，排序默认按照第一个元素，即索引的大小来排序
restored_sentence = []
original_list.sort()
for element in original_list:
    restored_sentence.append(element[1])
final_outcome= " ".join(restored_sentence)
print(f"final outcome:{final_outcome}")