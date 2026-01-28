import random
def random_sentence_scrambler():
    # 定义一些词汇库
    subjects = ["Gemini", "your cat", "my teacher", "an alien","Java","a keyboard"]
    verbs = ["fell in love with","destroyed","hacked into","is teaching","ate", "coded", "defeated", "messed up"]
    objects = ["Chatgpt", "a pepperoni pizza", "a blue laptop", "the leetcode contest","Python","a broken Macbook","the silicon valley"]

    # 随机拼接成一句话
    # random.choice()，在一个列表中随机抽取一个元素
    random_sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}"
    input_list = random_sentence.split()

    # 建立一个空列表，存储索引和元素：
    original_list = []
    for i in range(len(input_list)):
        element = input_list[i]
        original_list.append([i, element])

    # 带上索引，对input句子进行打乱
    # random.shuffle()对一个列表进行原地随机打乱
    random.shuffle(original_list)
    # 去掉索引，展示给用户：element由[索引，单词]的列表组成，所以取得下标为1的元素就能取得单词
    scrambled_list = []
    for element in original_list:
        scrambled_list.append(element[1])
    output_str = " ".join(scrambled_list)
    print(f"scrambled outcome:{output_str}")

    #用户开始猜测
    use_guess=input("plz restore the sentence:")
    if use_guess == random_sentence:
        print("BIG BRAIN!!! You nailed it!")
    else:
    #根据打乱后的句子，对句子进行还原: 先排序，排序默认按照第一个元素，即索引的大小来排序
        restored_sentence = []
        original_list.sort()
        for element in original_list:
            restored_sentence.append(element[1])
        final_outcome = " ".join(restored_sentence)
        print("Lame! Amateur!")
        print(f"final outcome:{final_outcome}.You're as slow as a ENIAC😠！")

if __name__ == "__main__":
    random_sentence_scrambler()