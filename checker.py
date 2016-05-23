from kwayHeap import kwayHeap
from heapq import *
from random import shuffle

"""
    There may or may not be code that you need to change, namely
        the import up top
        heapToString()
        get_heap()
        add()
        remove_min()
        get_min()
    but it's all just simple one line changes.

    If this works, it's very likely that your code works.

    I'll be testing your code with INPUT_SIZE = 1000 but setting it lower makes
    it easier to debug when it turns out that your heap is wrong.
"""
KSTOP = 10
INPUT_SIZE = 1000

#------------------------------------------------------------------------------#
#------------Start of the code you may or may not need to change---------------#
#------------------------------------------------------------------------------#

def heapToString(heap):
    """
        Returns the string form of your heap.

        For me, it prints [1, 7, 17] after I put 17, 7, and 1 into my heap.
        Modify this so that it works for your heap code. Perhaps change it to 
        something like
            str(heap._list)
        or just implement __str__() in your class.
    """
    return str(heap)

def get_heap(k):
    """
        Returns the heap that you implemented.

        Modify this so that it works for your heap code.
    """
    heap = kwayHeap(k)
    return heap

def add(heap, num):
    heap.add(num)

def remove_min(heap):
    return heap.remove_min()

def get_min(heap):
    return heap.min()

#------------------------------------------------------------------------------#
#--------------End of the code you may or may not need to change---------------#
#------------------------------------------------------------------------------#

def is_remove(s):
    return len(s) == 1

def is_add(s):
    return not is_remove(s)

def get_instructions(length):
    perm = []
    for i in range(length):
        perm.append('r')
        perm.append('a {0}'.format(i))
    shuffle(perm)
    num_of_things_contained = 0
    out = []
    end = []
    for s in perm:
        if is_add(s):
            num_of_things_contained += 1
            out.append(s)
        else:
            if num_of_things_contained > 0:
                num_of_things_contained -= 1
                out.append(s)
            else:
                end.append(s)
    for s in end:
        if num_of_things_contained > 0:
            num_of_things_contained -= 1
            out.append(s)
        else:
            print('get_instructions is wrong')
            break
    return out

def printHistory(history):
    print('key: line number, operation, result of operation')
    for i in range(len(history)):
        print(str(i + 1) + '\t' + history[i])

def checker(kstop, input_size):
    correct = True
    for k in range(1, kstop + 1):
        correct = correct and _checker(k, input_size)
    if correct:
        print('It seems to work =.= ... We\'ll see what happens on Friday.')

def _checker(k, LENGTH):
    yourHeap = get_heap(k)
    heap = []

    instructions = get_instructions(LENGTH)

    yourHeapHistory = []

    incorrect = False

    for i in range(1, LENGTH + 1):
        s = instructions[i - 1]
        if is_remove(s):
            try:
                you = remove_min(yourHeap)
            except:
                print('Error at line {0}\nTried to remove from empty heap'.\
                    format(i))
                incorrect = True
            try:
                correct = heappop(heap)
            except:
                print('Something is very wrong if you reach this line')
                break
            if you != correct:
                print('Error at line {0}\nWrong item removed. Expected {1}'.\
                    format(i, correct))
                incorrect = True
        else:
            num = int(s[2:])
            add(yourHeap, num)
            heappush(heap, num)
            you = get_min(yourHeap)
            correct = min(heap)
            if you != correct:
                print('Error at line {0}\nWrong value at root. Expected {1}'.\
                    format(i, correct))
                incorrect = True
        yourHeapHistory.append(s + '\t' + heapToString(yourHeap))

        if incorrect:
            printHistory(yourHeapHistory)
            break

    return not incorrect

checker(KSTOP, INPUT_SIZE)