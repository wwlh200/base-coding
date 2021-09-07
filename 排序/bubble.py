def bubble(arr):
    if len(arr) <= 1:
        return arr
    # 遍历次数
    for i in range(len(arr)):
        flag = False
        # 对比次数
        for j in range(len(arr)-1 - i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = True
        if not flag:
            break
    return arr

print(bubble([3, 8, 2, 4, 3, 1]))

