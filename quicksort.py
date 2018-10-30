def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        # 从后往前，遇见了比key更小的数，就把更小的数换到前面
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        # 从前往后，遇见了比key更大的数，把大数换到后面去
        lists[right] = lists[left]
    # 从key值分割开来，此时left=right
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

arr = [4,9,3,7,5,8]
print(quick_sort(arr,0,5))
