import random
from collections import deque
def s():
    m_d = []
    while len(m_d)<10:
        card = random.randint(0,9)
        if card not in m_d:
            m_d.append(card)
    return m_d

main_deck = s()
deck1 = deque([main_deck.pop() for i in range(5)])
print(f'First players cards {deck1}')
deck2 = deque([main_deck.pop() for i in range(5)])
print(f'Second players cards {deck2}')
step = 0
while (len(deck1)*len(deck2) != 0) and step < 1e6:
    f_p = deck1.popleft()
    s_p = deck2.popleft()
    if f_p == 0 and s_p == 9:
        deck1.append(f_p)
        deck1.append(s_p)
    elif f_p == 9 and s_p == 0:
        deck2.append(f_p)
        deck2.append(s_p)
    elif f_p < s_p:
        deck2.append(f_p)
        deck2.append(s_p)
    else:
        deck1.append(f_p)
        deck1.append(s_p)
    step += 1

if not deck1:
    print('second player ', step)
elif not deck2:
    print('first player ', step)
else:
    print('draw')