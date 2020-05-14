from functions import *


# standardization_without_interaction('ATGAGTAAAGGAGAAGAACTTTTCACTTAA', 'original')
# standardization_without_interaction('ATGAGTAACTAGTAAGAACTTTTCACTTAA', 'original')
# standardization_without_interaction('ATGTTTCTGCAACTAGTATTTGAATTCTAA', 'original')
# standardization()
# EAAT2_CDS_FASTA_Nucleiotide.txt  GFP_CDS_FASTA_Nucleiotide.txt
# EAAT2_CDS_GenBank.gb


def find_max(input):
    if input[0] == input[-1]:
        return input[0]
    else:
        ll = find_max(input[0:len(input) // 2])
        rr = find_max(input[len(input) // 2:len(input)])
        if ll > rr:
            print(' + ')
            return ll
        else:
            print(' + ')
            return rr


def merge_count(list):
    if len(list) <= 1:
        return list, 0
    mid = len(list) // 2
    left_li, left_cont = merge_count(list[:mid])
    right_li, right_cont = merge_count(list[mid:])
    count = left_cont + right_cont

    left_p, right_p = 0, 0
    result = []
    while left_p < len(left_li) and right_p < len(right_li):
        if left_li[left_p] > right_li[right_p]:
            result.append(left_li[left_p])
            count += len(right_li[right_p:])
            left_p += 1
        else:
            result.append(right_li[right_p])
            right_p += 1
    result += left_li[left_p:]
    result += right_li[right_p:]
    return result, count


def merge_count_2(list):
    if len(list) <= 1:
        return list, 0
    mid = len(list) // 2
    left_li, left_cont = merge_count_2(list[:mid])
    right_li, right_cont = merge_count_2(list[mid:])
    count = left_cont + right_cont
    result, count = merge(left_li, right_li, count)
    return result, count


def merge(B, C, count):
    p = len(B)
    q = len(C)
    i, j, k = 0, 0, 0
    A = [None] * (p + q - 1)
    while i < p and j < q:
        if B[i] > C[j]:
            A[k] = B[i]
            i += 1
            k += 1
            count += q - j
        else:
            A[k] = C[j]
            j += 1
            k += 1
    A[k:p + j] = B[i:p]
    A[p + j:q + p] = C[j:q]

    return A, count

    # result = []
    # while 0 < len(left_li) and 0 < len(right_li):
    #     if left_li[0] > right_li[0]:
    #         result.append(left_li.pop(0))
    #         count += len(right_li)
    #     else:
    #         result.append(right_li.pop(0))
    # result += left_li
    # result += right_li
    # return result, count


if __name__ == "__main__":
    mylist = [5, 5, 2, 4, 3, 1]
    print(mylist.index(5))
    # _, count = merge_count(mylist)
    # print(count)
    # _, count = merge_count_2(mylist)
    # print(count)
    print(find_max(mylist))
