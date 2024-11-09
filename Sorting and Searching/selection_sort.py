def selection_sort(arr):
    for i in range(len(arr)-1):
        mn = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[mn]:
                mn = j
        arr[i], arr[mn] = arr[mn], arr[i]
    return arr  

n = int(input("Input size: "))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)


# # one line space-separated input  
# n = int(input("Input size: "))
# x = input("Enter space-separated values: ")
# arr = list(map(int, x.split()))

selection_sort(arr)
print(arr)
