'''
归并排序是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
基本思路：
先递归的把数组划分为两个子数组，一直递归到数组中只有一个元素，然后再调用函数把两个子数组排好序，因为该函数在递归划分数组时会被压入栈，
所以这个函数真正的作用是对两个有序的子数组进行排序；
基本步骤：
1、判断参数的有效性，也就是递归的出口；
2、首先什么都不管，直接把数组平分成两个子数组；
3、递归调用划分数组函数，最后划分到数组中只有一个元素，这也意味着数组是有序的了；
4、然后调用排序函数，把两个有序的数组合并成一个有序的数组；
5、排序函数的步骤，让两个数组的元素进行比较，把大的/小的元素存放到临时数组中，如果有一个数组的元素被取光了，那就直接把另一数组的元素放到临时数组中，
    然后把临时数组中的元素都复制到实际的数组中；
https://www.cnblogs.com/chengxiao/p/6194356.html
时间复杂度O(n log n)
空间复杂度O(n)
稳定
'''

# 治
def merge(left, right):
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result

# 分
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    # //取整数
    middle = len(arr)//2
    left, right = arr[:middle], arr[middle:]
    return merge(mergeSort(left),mergeSort(right))

arr = [8,9,1,7,2,3,5,4,6,0]
arr = mergeSort(arr)
print(arr)

