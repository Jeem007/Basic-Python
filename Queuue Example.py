from collections import deque
#first in first out
bank=deque(["klara","Sofia","Boston"])
bank.popleft()
bank.popleft()
bank.popleft()
print(bank)
if not bank:
    print("No one in the bank now.")
