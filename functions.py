from csv import DictReader
# import numpy as np

from sequence import *


def read_file(input_file, input_type):
    if input_type == 'CSV':
        return read_CSV(input_file)
    elif input_type == 'Fasta':
        return read_Fasta(input_file)
    elif input_type == 'GenBank':
        return read_Genbank(input_file)
    elif input_type == 'txt':
        return read_txt(input_file)


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


def read_Fasta():
    pass


def read_Genbank():
    pass


def separate_seq(seq):  # separate a sequence into 3-words groups
    seq_in_3 = []
    for i in range(0, len(seq), 3):
        if i + 2 < len(seq):
            seq_in_3.append(seq[i] + seq[i + 1] + seq[i + 2])
    return seq_in_3


def mutation_rule(seq):  # 随机(顺序)突变
    legal, illegal_words = is_legal(seq)
    seq_in_3 = separate_seq(seq)
    standard_seq = seq_in_3
    if not legal:
        for key in illegal_words.keys():
            for sites in illegal_words[key]:
                x = seq_in_3[sites // 3]
                amino_acid = transfer(x)
                for amino_acid_names in codons:
                    if amino_acid == amino_acid_names.amino_acid:
                        for codon in amino_acid_names.codons:
                            if codon != x:
                                # temp = list(standard_seq)
                                standard_seq[sites // 3] = codon
                                standard_seq = ''.join(standard_seq)
                                print('The illegal restriction site is ' + key + ' in bp No.' + str(
                                        sites) + '\nChange ' + x + ' to ' + codon)
                                break
    legal, illegal_words = is_legal(standard_seq)
    if legal:
        return standard_seq
    else:
        return mutation_rule(standard_seq)
