# collections -> deque

import collections
st = collections.deque()
print(st)

st.append(10)
st.append(20)
st.append(30)
print(st)

print(st.pop())
print(not st)
print(st[-1])



# # queue -> LIFO Queue

# import queue
# st = queue.LifoQueue()
# st.put(10)
# st.put(20)
# st.put(30)

# print(st.get())
# print(st.get())
# print(st.get())



# # timeout

# import queue
# st = queue.LifoQueue(3)
# st.put(10)
# st.put(20)
# st.put(30)

# print(st.get())
# print(st.get())
# print(st.get())
# print(st.get(timeout=1))