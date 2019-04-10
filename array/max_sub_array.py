#coding:utf-8
'''
def max_subarray(array):
    if array == None or len(array)<1:
        print("illegal")
        return
    ThisSum = 0
    MaxSum = 0
    i = 0
    while i < len(array):
        j = i
        while j < len(array):
            ThisSum = 0
            k = i
            while k < j:
                ThisSum +=array[k]
                k += 1
            if ThisSum >MaxSum:
                MaxSum = ThisSum
            j += 1
        i += 1
    return MaxSum
'''
def max_subarray(array):
    if array == None or len(array)<1:
        print("illegal")
        return
    maxSum = -2 **31
    i = 0
    while i<len(array):
        sums = 0
        j = i
        while j < len(array):
            sums += array[j]
            if sums >maxSum:
                maxSum = sums
            j += 1
        i +=1
    return maxSum
if __name__ == "__main__":
    array = [1,-2,4,8,-4,7,-1,-5]
    print(max_subarray(array))
