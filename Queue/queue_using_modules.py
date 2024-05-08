# # appendleft,  pop

# import collections
# q = collections.deque()
# print(q)

# q.appendleft(10)
# q.appendleft(20)
# q.appendleft(30)
# print(q)

# q.pop()
# print(q)



# # append,  popleft

# import collections
# q = collections.deque()

# q.append(10)
# q.append(20)
# q.append(30)
# print(q)

# q.popleft()
# print(q)



#  queue -> Queue

import queue
q = queue.Queue()

q.put(10)
q.put(20)
q.put(30)

print(q.get())