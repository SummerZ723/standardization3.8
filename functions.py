from csv import DictReader
from Bio import SeqIO
from Codon import amino_acid_list
from sequence import *
import prettytable as pt

table = pt.PrettyTable()


def read_file(input_file, input_type):
    if input_type == 'CSV':
        return read_CSV(input_file)
    elif input_type == 'original':
        return input_file
    elif input_type == 'fasta' or 'genbank':
        return read_Fasta_Genbank(input_file, input_type)
    elif input_type == 'txt':
        return read_txt(input_file)
    else:
        print('对不起，您输入的序列格式不正确！')


def read_CSV(input_file, sep=","):
    list_seq = []
    reader = DictReader(open(input_file), delimiter=sep, quotechar='"')
    for l in reader:
        list_seq.append(l)
    return list_seq


def read_txt(input_file):
    with open(input_file, 'r') as f:
        seq = f.read()
    return seq


def read_Fasta_Genbank(file, file_type):
    seq = SeqIO.read(file, file_type)
    complete_seq = str(seq.seq)
    return complete_seq


def separate_seq(seq):  # 将普通序列分为密码子序列
    seq_in_3 = []
    for i in range(0, len(seq), 3):
        if i + 2 < len(seq):
            seq_in_3.append(seq[i] + seq[i + 1] + seq[i + 2])
    return seq_in_3


def mutation_rule(seq, illegal_words):  # 随机(顺序)突变
    output_seq = ''
    seq_in_3 = separate_seq(seq)
    output_in_3 = seq_in_3
    for key in illegal_words.keys():
        for sites in illegal_words[key]:
            codon_be_changed = seq_in_3[sites // 3]
            codons_of_this_aa = transfer(codon_be_changed)
            for codon_change_to in codons_of_this_aa:
                if codon_change_to != codon_be_changed:
                    output_in_3[sites // 3] = codon_change_to
                    output_seq = ''.join(output_in_3)
                    table.add_row([key, str(sites), codon_be_changed, codon_change_to])
                    # print('*     ' + key + ' in bp No.' + str(
                    #     sites) + '\n* --> Change ' + codon_be_changed + ' to ' + codon_change_to)
                    break
    legal, illegal_words = check_legal(output_seq)
    if legal:
        return output_seq
    else:
        return mutation_rule(output_seq, illegal_words)


def add_prefix_suffix(seq):  # 序列前后缀标准化
    return 'GAATTCGCGGCCGCTTCTAG ' + seq + ' TACTAGTAGCGGCCGCTGCAG'


def transfer(seq):  # 密码子对应的同义密码子
    for x in amino_acid_list:
        if seq in x.codons:
            return x.codons


def standardization():
    input_file = input('请输入序列文件:\n')
    input_type = input('请输入文件类型：（支持fasta,genbank,txt,csv及原始序列original）\n')
    seq = read_file(input_file, input_type)
    print('您输入的序列为： ' + seq)
    legal, illegal_words = check_legal(seq)
    if legal:
        print('该序列不存在非法酶切位点。')
        standard_seq = add_prefix_suffix(seq)
    else:
        table.field_names = ['Illegal restriction enzyme', 'Site/bp No.', 'Origin codon', 'New codon']
        seq = mutation_rule(seq, illegal_words)
        standard_seq = add_prefix_suffix(seq)
        print(table)
    print('标准化后的序列为： ' + standard_seq + '\n')


def standardization_without_interaction(input_file, input_type):
    seq = read_file(input_file, input_type)
    print('您输入的序列为： ' + seq)
    legal, illegal_words = check_legal(seq)
    if legal:
        print('该序列不存在非法酶切位点。')
        standard_seq = add_prefix_suffix(seq)
    else:
        table.field_names = ['Illegal restriction enzyme', 'Site/bp No.', 'Origin codon', 'New codon']
        seq = mutation_rule(seq, illegal_words)
        standard_seq = add_prefix_suffix(seq)
        print(table)
    print('标准化后的序列为： ' + standard_seq + '\n')
