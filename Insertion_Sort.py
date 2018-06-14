# Worst case    O(n^2)
# Best case     O(n)
# Avg case      O(n^2)
# Worst-case space complexity O(n), O(1) auxiliary

def Insertion_Sort_up(n):
    length = len(n)
    # i = 0
    for j in range(1, length):
        # print("j = ", j)
        # x = n[j]
        while n[j] < n[j-1] and j >= 1:
            n[j], n[j-1] = n[j-1], n[j]	# this maybe not insertion sort but bubble sort, ref to "Data structure(Rence) page140"
            j -= 1
            # print(n)  # print the process of the function
    return n

def Insertion_Sort_down(n):
    length = len(n)
    # i = 0
    for j in range(1, length):
        # print("j = ", j)
        # x = n[j]
        while n[j] > n[j-1] and j >= 1:
            n[j], n[j-1] = n[j-1], n[j]
            j -= 1
            # print(n)  # print the process of the function
    return n



if __name__ == "__main__":
    import numpy
    n = list(numpy.random.randint(0,100,20))
    print("n is \t\t\t", n)
    sort_n_up = Insertion_Sort_up(n)
    print("sorted n_up is \t", sort_n_up)
    sort_n_down = Insertion_Sort_down(n)
    print("sorted n_down is", sort_n_down)



    #=====Test whether up and down lists are right sorted.
    sort_n_down.reverse()
    if sort_n_up == sort_n_down:
        print("TRUE: up = down.reverse")
    else:
        print("ERROR: up != down.reverse")
    #========================================================