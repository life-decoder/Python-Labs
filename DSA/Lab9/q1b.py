""" 
Question 1b: Air-Traffic Control Simulation
An airport is developing a computer simulation of air-traffic control that handles events such as
landings and take-offs. Each event has a reference and a timestamp that denotes the time when
the event occurs. The simulation program needs to efficiently perform the following two
fundamental operations:
- Insert an event with a given reference and timestamp (that is, add a future event).
- Extract the event with the smallest timestamp (that is, determine the next event to
  process) and display the event reference.
Implement the simulation program.
"""


class EventQueue:
  def __init__(self):
    self.events = []

  def isEmpty(self):
    return len(self.events) == 0

  def insert(self, reference, timestamp):
    newEvent = (timestamp, reference)
    self.events.append(newEvent)
    self._bubble_up(len(self.events) - 1)

  def extractNextEvent(self):
    if self.isEmpty():
      return None

    nextEvent = self.events[0]
    lastEvent = self.events.pop()

    if not self.isEmpty():
      self.events[0] = lastEvent
      self._bubble_down(0)

    return nextEvent

  def _bubble_up(self, index):
    parent = (index - 1) // 2

    while index > 0 and self.events[index][0] < self.events[parent][0]:
      self.events[index], self.events[parent] = self.events[parent], self.events[index]
      index = parent
      parent = (index - 1) // 2

  def _bubble_down(self, index):
    size = len(self.events)

    while True:
      leftChild = 2 * index + 1
      rightChild = 2 * index + 2
      smallest = index

      if leftChild < size and self.events[leftChild][0] < self.events[smallest][0]:
        smallest = leftChild

      if rightChild < size and self.events[rightChild][0] < self.events[smallest][0]:
        smallest = rightChild

      if smallest == index:
        break

      self.events[index], self.events[smallest] = self.events[smallest], self.events[index]
      index = smallest


def main():
  eventQueue = EventQueue()

  events = [
    ("Landing-101", 15),
    ("Takeoff-202", 4),
    ("Landing-303", 12),
    ("Takeoff-404", 7),
    ("Landing-505", 20),
  ]

  for reference, timestamp in events:
    eventQueue.insert(reference, timestamp)

  print("Events processed in timestamp order:")
  while not eventQueue.isEmpty():
    timestamp, reference = eventQueue.extractNextEvent()
    print(reference)


if __name__ == "__main__":
  main()
