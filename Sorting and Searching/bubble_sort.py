def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j-1]>arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

n = int(input("Input size: "))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)


# # one line space-separated input  
# n = int(input("Input size: "))
# x = input("Enter space-separated values: ")
# arr = list(map(int, x.split()))

bubble_sort(arr)
print(arr)
