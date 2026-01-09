n = input("Enter some numbers: ")

nums = n.split()
sum = 0

for i in nums:
    sum = sum + int(i)

print(sum)