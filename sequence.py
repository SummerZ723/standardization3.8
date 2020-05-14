def check_seq(seq):  # 判断是否ATGC序列以及是否为3的倍数
    for x in seq:
        if x not in ['A', 'T', 'G', 'C']:
            print('错误：该序列出现非法脱氧核苷酸！')
            return False
    if len(seq) % 3 != 0 or not seq.startswith('ATG'):
        print('错误：该序列非CDS序列！')
        return False
    if seq == '':
        print('错误：该序列为空序列！')
        return False
    return True


def check_legal(seq):  # 判断有无非法酶切位点及其对应序号
    legal = True
    illegal_words = {'GAATTC': [], 'TCTAGA': [], 'ACTAGT': [], 'CTGCAG': [], 'GCGGCCGC': []}
    for sites in illegal_words.keys():
        beg = 0
        while seq.find(sites, beg) != -1:
            position = seq.find(sites, beg)
            if position != -1:
                legal = False
                illegal_words[sites].append(position)
            beg = position + 1
    return legal, illegal_words


def delete():  # 酶切位点删除
    pass


class Sequence:

    def __init__(self, seq):
        self.seq = seq.upper()
        self.legal, self.illegal_words = check_legal(seq)
