from typing import Any
import sys

class FixedStack:

    def __init__(self, capacity: int = 10000) -> None:
        self.stk = [None]*capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr
    
    def empty(self) -> int:
        if self.ptr == 0:
            return 1
        else:
            return 0
    
    def push(self, value: Any) -> None:
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.empty():
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def size(self) -> int:
        return self.ptr
    
    def top(self) -> Any:
        if self.empty():
            return -1
        return self.stk[self.ptr-1]
    
s = FixedStack()

n = int(input())
for i in range(n):
    c = sys.stdin.readline().split()
    if len(c) == 2:
        s.push(int(c[1]))
    else:
        if c[0] == "pop":
            print(s.pop())
        elif c[0] == "size":
            print(s.size())
        elif c[0] == "empty":
            print(s.empty())
        else:
            print(s.top())
