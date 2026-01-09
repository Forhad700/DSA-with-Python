table_size = 10
hash_table = [[] for _ in range(table_size)]

def hashing(key):
  return hash(key)%table_size
  
def insert(key, value):
  index = hashing(key)
  for item in hash_table[index]:
    if item[0]==key:
      item[1]=value
      return
  hash_table[index].append([key, value])
  
def search(key):
  index = hashing(key)
  for item in hash_table[index]:
    if item[0]==key:
      return item[1]
  return None
  
def delete(key):
  index = hashing(key)
  for i, item in enumerate(hash_table[index]):
    if item[0]==key:
      del hash_table[index][i]
      return True
  return False
  
def dis():
  for i, item in enumerate(hash_table):
    print(i, item)
    

dis()

insert('a', 'apple')
insert('b', 'bat')
insert('c', 'cat')

print('After Insertion')
dis()

print(search('a'))

if delete('a'):
  print("Deleted")
else:
  print('Key is not found')
  
print('After Deletion')
dis()