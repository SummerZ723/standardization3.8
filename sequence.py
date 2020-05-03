from functions import *
from Codon import *


def is_seq(seq):  # 判断是否ATGC序列以及是否为3的倍数
    for x in seq:
        if x not in ['A', 'T', 'G', 'C']:
            return False
    if len(seq) % 3 != 0:
        return False
    return True
    # dict_seq = {}
    # for s in seq:
    #     dict_seq[s] = seq.count(s)
    # if len(dict_seq) != 4:
    #     return False
    # else:
    #     return True


def is_legal(seq):  # 判断有无非法酶切位点及其对应序号
    legal = True
    illegal_words = {'GAATTC': [], 'TCTAGA': [], 'ACTAGT': [], 'CTGCAG': [], 'GCGGCCGC': []}
    for sites in ['GAATTC', 'TCTAGA', 'ACTAGT', 'CTGCAG', 'GCGGCCGC']:
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


def add_prefix_suffix():  # 序列前后缀标准化
    pass


def transfer(seq):  # 密码子对应的氨基酸
    for x in codons:
        if seq in x.codons:
            return x.amino_acid


class Sequence:
    # seq = ''
    # legal = True
    # normalization = True
    # illegalWords = {'GAATTC': None, 'TCTAGA': None, 'ACTAGT': None, 'CTGCAG': None, 'GCGGCCGC': None}

    def __init__(self, seq):
        self.seq = seq.upper()
        self.legal, self.illegal_words = is_legal(seq)


if __name__ == '__main__':
    seq = 'ATGGAATTCTCTAGAACTAGTCTGCAGGCGGCCGCTAA'
    testSequenceGFP = 'ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGG' \
                   'TGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCGGTTATGGTGTTCAAT' \
                   'GCTTTGCGAGATACCCAGATCATATGAAACAGCATGACTTTTTCAAGAGTGCCATGCCTGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGG' \
                   'AACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACA' \
                   'CAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATG' \
                   'GAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCG' \
                   'AAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAA'
    print(mutation_rule(seq))
    print(mutation_rule(testSequenceGFP))

