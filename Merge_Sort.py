# Worst case    O(nlogn)
# Best case     O(nlogn)
# Avg case      O(nlogn)
# Worst-case space complexity O(n), O(1) auxiliary


def Merge(l_n, r_n):

    len_l = len(l_n)
    len_r = len(r_n)

    i = 0
    j = 0
    merge_n = []

    while i<len_l and j <len_r:
        if l_n[i] <= r_n[j]:
            merge_n.append(l_n[i])
            i += 1
        else:
            merge_n.append(r_n[j])
            j += 1

    if i <= len_l:
        merge_n += l_n[i : ]
    if j <= len_r:
        merge_n += r_n[j : ]

    return merge_n


def Merge_Sort(n):

    if len(n) <= 1:
        return n

    mid_po = int(len(n)/2)
    l_n = Merge_Sort(n[:mid_po])
    r_n = Merge_Sort(n[mid_po:])

    return Merge(l_n, r_n)


if __name__ == "__main__":
    import numpy
    n = list(numpy.random.randint(0, 100, 10))
    print("n is \t\t\t", n)

    x = Merge_Sort(n)
    print(x)




