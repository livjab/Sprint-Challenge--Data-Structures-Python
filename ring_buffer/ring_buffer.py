# new git branch
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.oldest = 0

  def append(self, item):

      if self.current < self.capacity:
          # remove Nones
          self.storage.pop(0)
          # Then append item
          self.storage.append(item)
          # increase count
          self.current +=1

      elif self.current == self.capacity:
          self.storage.pop(self.oldest)
          self.storage.insert(self.oldest, item)
          self.oldest +=1

      else:
          pass

  def get(self):
      return [i for i in self.storage if i]

"""
buffer = RingBuffer(3)
print(buffer.get())

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())
print(buffer.storage)

buffer.append('d')

print(buffer.get())

buffer.append('e')
buffer.append('f')

print(buffer.get())
"""
