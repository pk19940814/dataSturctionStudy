from collections import deque
from queue import Queue


# 用list实现队列
class MyQueue(object):
    def __init__(self):
        self.items = []

    def enter(self, item):
        return self.items.insert(0, item)

    def out(self):
        return self.items.pop()

    def dsise(self):
        return len(self.items)


# 手捧雷
def dkill(name, num):
    d = deque()
    for i in name:
        d.appendleft(i)
    while len(d) > 1:
        for i in range(num):
            d.appendleft(d.pop())
        print('kill', d.pop())
    return 'alive:%s' % d.pop()


def kill(name, num):
    a = Queue()
    for i in name:
        a.put(i)
    while a.qsize() > 1:
        for i in range(num):
            a.put(a.get())
        print('kill', a.get())
    return 'alive: %s' % a.get()

print(kill(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 9))
print('----------------')
print(kill(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 9))
