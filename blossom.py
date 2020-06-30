#The underlying data structure for Blossom is going to be a key-value store that uses the common names for flowers as the key and saves the floral meaning of the flower as the value.

from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for number in range(size)]

  #Generate a unique hash code for any given key
  def hash(self, key):
    return sum(key.encode())
  
  #Convert the hash code into an array index to use with self.array 
  def compress(self, hash_code):
    return hash_code % self.array_size

  #Place a key value pair at the index given by compress
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    #self.array[array_index] = [key,value]
    payload = Node([key,value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
        return
    list_at_array.insert(payload)

  #Retrun the value of a given key
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    #if payload =! None and payload[0] == key:
      #return payload[1]
    #else:
      #return None
    for item in list_at_index:
      if item[0] == key:
        return item[1]
      return None

blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
  #print(flower)
  blossom.assign(flower[0], flower[1])


print(blossom.retrieve('snapdragon'))
