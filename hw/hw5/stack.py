class StackItem:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    return self.value


class Stack:
  def __init__(self, items=[]):
    self.length = 0
    self.first = None

    for item in items:
      self.push(item)

  def __len__(self):
    return self.length

  def __str__(self):
    res = []

    item = self.first
    while (item is not None):
      res.append(item.value)
      item = item.next

    return "{} item(s): [{}]".format(self.length, " <-- ".join(list(map(str, res))))

  @property
  def empty(self):
    return self.first is None

  def push(self, value):
    temp = self.first
    self.first = StackItem(value)
    self.first.next = temp

    self.length += 1

    return self

  def pop(self):
    if (self.empty):
      raise('No items in stack')

    value = self.first.value
    self.first = self.first.next

    return value