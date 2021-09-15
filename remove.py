
# 把两个数组去重 [123],[2334],[1,4]
# 将两个数组合并
# 通过快排对数据排序
# 将一个的存入数组, 计入临时数据存储

def quick_sort(arr):
    if len(arr) < 1:
        return arr

    mid = arr.pop(0)
    left, right = [], []
    for value in arr:
        left.append(value) if value < mid else right.append(value)
    return quick_sort(left)+[mid]+quick_sort(right)


def remove_arrs(arr1, arr2):
    sort_arr = quick_sort(arr1+arr2)
    repeat_num = None
    ret_nums = []

    for num in sort_arr:
        if num != repeat_num:
            ret_nums.append(num)
        elif ret_nums[len(ret_nums)-1] == repeat_num:
            ret_nums.pop()
        repeat_num = num
    return ret_nums


print(remove_arrs([1,8,3,4,5,6,5,5,3,2423, 2, 3], [2, 3, 3, 4]))
