def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] >= pivot:
            left = left + 1
        while arr[right] <= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right


def find_kth_largest(arr, n, k):
    quick_sort(arr, 0, n - 1)
    return arr[k - 1]


a = [3, 2, 1, 5, 6, 4]
n = len(a)
k = 2
print(find_kth_largest(a, n, k))

"""有一个整数数组，请你根据快速排序的思路，找出数组中第K大的数。
给定一个整数数组a,同时给定它的大小n和要找的K(K在1到n之间)，请返回第K大的数，保证答案存在。用 Python 求解"""