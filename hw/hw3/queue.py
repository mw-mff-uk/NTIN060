class QueueItem:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


class Queue:
  def __init__(self, items=[]):
    self.first = None
    self.last = None
    self.length = 0

    for item in items:
      self.enqueue(item)

  def __len__(self):
    return self.length

  def __str__(self):
    item = self.first
    res = []

    while (item is not None):
      res.append(item.value)
      item = item.next

    return "[" + " <-- ".join(list(map(str, res))) + "]"

  @property
  def empty(self):
    return self.first is None

  def enqueue(self, value):
    item = QueueItem(value)

    if (self.empty):
      self.first = item
      self.last = item
    else:
      self.last.next = item
      self.last = item

    self.length += 1

    return self

  def dequeue(self):
    if (self.empty):
      raise Exception("No items in queue")

    value = self.first.value
    self.first = self.first.next

    if (self.empty):
      self.last = None

    self.length -= 1

    return value