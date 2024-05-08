def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input("Input size: "))
lst = []
for i in range(n):
    val = int(input())         # or,  lst.append(int(input()))   
    lst.append(val)

# # one line space-separated input  
# n = int(input("Input size: "))
# val = input("Enter space-separated values: ")
# lst = list(map(int, val.split()))

bubble_sort(lst)
print(lst)