# # pivot position at First index
# def pivot_pos(arr, first, last):
#     pivot = arr[first]
#     left = first+1
#     right = last
#     while True:
#         while left<=right and arr[left]<=pivot:
#             left = left+1
#         while left<=right and arr[right]>=pivot:
#             right = right-1
#         if right<left:
#             break
#         else:
#             arr[left], arr[right] = arr[right], arr[left]
#     arr[first], arr[right] = arr[right], arr[first]
#     return right


# pivot position at Last index
def pivot_pos(arr, first, last):
    pivot = arr[last]
    left = first
    right = last-1
    while True:
        while left<=right and arr[left]<=pivot:
            left = left+1
        while left<=right and arr[right]>=pivot:
            right = right-1
        if right<left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[last], arr[left] = arr[left], arr[last]
    return left

def quick_sort(arr, first, last):
    if first<last:
        p = pivot_pos(arr, first, last)
        quick_sort(arr, first, p-1)
        quick_sort(arr, p+1, last)


n = int(input("Input size: "))
val = input("Enter space seperated values: ")
arr = list(map(int, val.split()))

quick_sort(arr, 0, n-1)
print(arr)