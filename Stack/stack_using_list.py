# # simple stack implement using list
# st = []
# st.append(10)
# st.append(20)
# st.append(30)
# st.append(40)

# print(st)
# print(st[-1])

# st.pop()
# st.pop()
# st.pop()

# print(st)

# st.pop()
# print(st)

# print(len(st)==0)
# print(not st)




# stack implement using list with funtions

st = []
def push():
    if len(st)==n:
        print("List is full")
    else:
        element = input("Input Element: ")
        st.append(element)
        print(st)

def pop_element():
    if not st:
        print("List is empty")
    else:
        e = st.pop()
        print("Remove element is ", e)
        print(st)

n = int(input("Input size: "))
while True:
    print("Select option: 1.Push 2.Pop 3.Quit")
    op = int(input())
    if op==1:
        push()
    elif op==2:
        pop_element()
    elif op==3:
        break
    else:
        print("Invalid option")