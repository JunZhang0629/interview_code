#类快速排序的方法找出数组中第k大的值
def findk_small(array,low,high,k):
    i = low
    j = high
    splitElem = array[i]
    while i < j:
        while i < j and array[j] >= splitElem:
            j -= 1
        if i < j:
            array[i] = array[j]
            i += 1
        while i < j and array[i] <= splitElem:
            i += 1
        if i < j:
            array[j] = array[i]
            j -= 1
    array[i] = splitElem
    subArrayIndex = i - low
    if subArrayIndex == k-1:
        return array[i]
    elif subArrayIndex > k-1:
        return findk_small(array,low,i-1,k)
    else:
        return findk_small(array,i+1,high,k-(i-low)-1)

if __name__== "__main__":
    array = [4,0,1,0,2,3]
    k = 3
    print(findk_small(array,0,len(array)-1,k))
