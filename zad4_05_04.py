from collections import deque

first_player=deque(list(map(int, input().split())))
second_player=deque(list(map(int, input().split())))
step=0
while step<1e6 and len(first_player)*len(second_player):
    first_player_card=first_player.popleft()
    second_player_card=second_player.popleft()
    if first_player_card==0 and second_player_card==9:
        first_player.append(first_player_card)
        first_player.append(second_player_card)
    elif first_player_card==9 and second_player_card==0:
        second_player.append(first_player_card)
        second_player.append(second_player_card) 
    elif first_player_card>second_player_card:
        first_player.append(first_player_card)
        first_player.append(second_player_card) 
    else:
        second_player.append(first_player_card)
        second_player.append(second_player_card)
    step+=1

if not first_player:
    print("second",step)
elif not second_player:
    print("second",step)
else:
    print("botva")