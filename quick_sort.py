# Worst case    O(n^2)
# Best case     O(nlogn)
# Avg case      O(nlogn)
# Worst-case space complexity "depends on case"

# Three ways to write the quicksort method, and the speed is as following:
#    QS_3 > QS_1 > QS_2



ii = []

def QS_1(n_list):
# switch the i and j
#     print("NEW QS()<=========>")
    if len(n_list) <= 1:
        return n_list

    i = 0
    j = len(n_list) - 1
    po = 0
    pivot = n_list[po]
    # print("pivot is %d(po = %d)"%(pivot, po))

    while i < j:
        # print("\n>>>>>>>>>>>>>>")
        while j > i and n_list[j] > pivot:
            j -= 1
        while i < j and n_list[i] <= pivot:
            i += 1
        # print("%d(i = %d) changed with %d(j = %d)"%(n_list[i],i,n_list[j],j))
        # print("n_list is ",n_list)
        n_list[i], n_list[j] = n_list[j], n_list[i]
        # print("after >>>", n_list)

    # print("\n")
    # if n_list[i] < pivot:
    n_list[i], n_list[po] = pivot, n_list[i]
    # else:
    #     n_list[i-1], n_list[po] = pivot, n_list[i-1]
    # print(n_list)
    next_l = n_list[ : i]
    next_r = n_list[i + 1 :]
    QS_1(next_l)
    QS_1(next_r)
    return n_list

#==============================================================================
def QS_2(n_list):
# change the value one by one, like "1.j -> po; 2.i -> j; 3.j -> i

    # print(">>>>>>>>>>>>")
    if len(n_list) <= 1:
        return n_list

    pivot = n_list[0]
    i = 0
    j = len(n_list) - 1
    while i < j:
        p = i
        while i < j and n_list[j] > pivot and j >= 0:
            j -= 1
        n_list[p] = n_list[j]
        p = j
        # print("J == > %r"%n_list)
        while i < j and n_list[i] <= pivot and i < len(n_list):
            i += 1
        n_list[p] = n_list[i]
        # print(" == > %r" % n_list)

    n_list[i] = pivot
    # print(n_list)
    # sys.exit(1)

    left_n = n_list[ : i]
    # print(left_n)
    right_n = n_list[i + 1 :]
    # print(right_n)

    QS_2(left_n)
    QS_2(right_n)
    return n_list


#===================================================================================
def QS_3(n_list):
# scan the list and pop the item to the blanc list
#     print("new QS_3 ====>")
    if len(n_list) <= 1:
        # print("-_-!! last and n is", n_list)
        return n_list

    l = []
    r = []
    base = n_list[0]
    # print("n_list is ", n_list)
    # print(base)

    #------
    for item in n_list:
        if item < base:
            l.append(item)
        elif item > base:
            r.append(item)
    


    #------


    # l = [item for item in n_list if item < base]
    # # print(l)
    # r = [item for item in n_list if item > base]
    # # print(r)
    middle = [base]*(len(n_list) - len(l) - len(r))
    # print(middle)

    return QS_3(l) + middle + QS_3(r)

#====================================================================================

if __name__ == '__main__':

    import time
    import timeit
    import numpy
    import sys

    # global n_list
    n_list = numpy.random.randint(0, 10000, 1000)

    # start = time.clock()

    # n = [13, 42, 9, 55, 23, 18, 87, 47, 99, 65, 0, 5, 78, 84]
    n_copy = n_list[:]
    n_1 = n_list[:]
    n_2 = n_list[:]
    n_3 = n_list[:]
    n_4 = n_list[:]
    n_5 = n_list[:]
    n_6 = n_list[:]
    # print("n_copy is ", n_copy)
    # print("length of n is %d"%(len(n)))
    # print("==================>")
    # print(n_copy)

    fun = [QS_3, QS_2, QS_3]


    #====> start test =====>

    t = 50
    n_iter = [n_list[:] for i in range(t)]
    time_list = []

    for i in range(t):
        start_1 = time.clock()
        # start_1 = time.time()
        x = list(fun[0](n_iter[i]))
        # end_1 = time.time()
        # print("x >>> ", (end_1 - start_1) * 1000)
        time_list.append((time.clock() - start_1)*1000)
        # print("x >>> ", time_list[i])
        # print(x)
    avg_t = sum(time_list[1:])/(t-1)
    print("x => ", avg_t)

    n_iter_x = [n_list[:] for i in range(t)]
    n_iter_y = [n_list[:] for i in range(t)]
    n_iter_z = [n_list[:] for i in range(t)]

    test_x_y_z = []
    for i in range(t):
        x = list(fun[0](n_iter_x[i]))
        y = list(fun[1](n_iter_y[i]))
        z = list(fun[2](n_iter_z[i]))
        if x == y and x == z and y == z:
            test_x_y_z.append(True)
        else:
            test_x_y_z.append(False)

    print(all(test_x_y_z))

#======================================
    #
    # start_2 = time.clock()
    # # start_2 = time.time()
    # y = list(fun[0](n_2))
    # # end_2 = time.time()
    # # print("y >>> ", (end_2 - start_2) * 1000)
    # print("y >>> ", (time.clock() - start_2)*1000)
    # # print(y)
    # # print(type(y))
    #
    # start_3 = time.clock()
    # # start_3 = time.time()
    # z = list(fun[0](n_3))
    # # end_3 = time.time()
    # # print("z >>> ", (end_3 - start_3) * 1000)
    # print("z >>> ", (time.clock() - start_3)*1000)
    # # print(z)
    # # print(len(z))
    #
    # start_4 = time.clock()
    # # start_4 = time.time()
    # x = list(fun[0](n_4))
    # # end_1 = time.time()
    # # print("x >>> ", (end_1 - start_1) * 1000)
    # print("x >>> ", (time.clock() - start_4) * 1000)
    # # print(x)
    #
    # start_5 = time.clock()
    # # start_2 = time.time()
    # y = list(fun[0](n_5))
    # # end_2 = time.time()
    # # print("y >>> ", (end_2 - start_2) * 1000)
    # print("y >>> ", (time.clock() - start_5) * 1000)
    # # print(y)
    # # print(type(y))
    #
    # start_6 = time.clock()
    # # start_3 = time.time()
    # z = list(fun[0](n_6))
    # # end_3 = time.time()
    # # print("z >>> ", (end_3 - start_3) * 1000)
    # print("z >>> ", (time.clock() - start_6) * 1000)
    # # print(z)
    # # print(len(z))


    # if x == y and x == z and y == z:
    #     print(True)
    # else:
    #     print(False)

    # print("n_copy is ", n_copy)
    # print("x is ", x)
    # print((time.clock() - start)*1000)
