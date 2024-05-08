# # priority queue using list

# q = []
# q.append(10)
# q.append(30)
# q.sort()
# q.append(20)
# q.sort()
# print(q)

# q.pop(0)
# print(q)
# q.pop(0)
# print(q)
# q.pop(0)
# print(q)



# # priority queue using PriorityQueue
# # taking lowest priority

# import queue
# q = queue.PriorityQueue()

# q.put(10)
# q.put(50)
# q.put(20)
# q.put(40)
# q.put(40)

# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())


# taking highest priority

q = []
q.append((1, "alexa"))
q.append((4, "alex"))
q.append((2, "al"))
q.sort(reverse=True)
print(q)

print(q.pop(0))