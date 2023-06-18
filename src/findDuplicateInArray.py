'''

'''
import time

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def chkDuplicate(lst):
    tmp = None
    for i in range(len(lst)):
        if tmp == lst[i]:
            break
        tmp = lst[i]
    return tmp

print('Start!')
start_time = time.time()

l = [1, 11, 9, 4, 6, 7, 2, 1]
l = bubbleSort(l)

print(f'The duplicate is {chkDuplicate(l)}')
print("--- %s seconds ---" % (time.time() - start_time))


''''''''''''
