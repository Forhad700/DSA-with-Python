def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i-1
        while j>=0 and arr[j]>curr:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = curr

n = int(input("Input size: "))
val = input("Enter space seperate values: ")
arr = list(map(int, val.split()))
insertion_sort(arr)
print(arr)