'''

1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 重复第二步，直到所有元素均排序完毕。

选择排序
时间复杂度O(n^2)
空间复杂度O(1)
'''

arr = [9,8,7,6,5,4,3,2,1]

def selection_sort(arr):

    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[i],arr[minIndex]
    return arr

arr = selection_sort(arr)
print(arr)

