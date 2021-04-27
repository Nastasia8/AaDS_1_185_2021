from collections import dequez

list_first = input().split()
list_first = deque([int(list_first[i]) for i in range(5)])

list_second = input().split()
list_second = deque([int(list_second[i]) for i in range(5)])
step = 0

while step < 1e6 and len(list_first)*len(list_second):
    card1 = list_first.popleft()
    card2 = list_second.popleft()
    if card1 == 0 and card2 == 9:
        list_first.append(card1)
        list_first.append(card2)
    elif card1 == 9 and card2 == 0:
        list_second.append(card1)
        list_second.append(card2)
    elif card1 < card2:
        list_second.append(card1)
        list_second.append(card2)
    else:
        list_first.append(card1)
        list_first.append(card2)
    step += 1

if not list_first:
    print("second", step)
elif not list_second:
    print("first", step)
else:
    print("botva")