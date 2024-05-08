# q = []
# q.append(10)
# q.append(20)
# q.append(30)
# print(q)

# q.pop(0)
# print(q)

# q.pop(0)
# print(q)


# q = []
# q.insert(0,10)
# q.insert(0,20)
# q.insert(0,30)
# print(q)

# q.pop()
# print(q)


# stack implement using list with funtions

q = []
def enqueue():
    element = input("Input Element: ")
    q.append(element)
    print(element, "is added to queue")

def dequeue():
    if not q:
        print("Queue is empty")
    else:
        e = q.pop(0)
        print("Remove element is ", e)

def display():
    print(q)

while True:
    print("Select option: 1.Add 2.Remove 3.Show 4.Quit")
    op = int(input())
    if op==1:
        enqueue()
    elif op==2:
        dequeue()
    elif op==3:
        display()
    elif op==4:
        break
    else:
        print("Invalid option")