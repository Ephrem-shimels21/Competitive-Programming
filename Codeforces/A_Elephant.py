friends_house = int(input())
move = 5
total = 0
while friends_house:
    if friends_house >= move:
        full_move = friends_house // move
        total += full_move
        friends_house = friends_house - (move * full_move)
    move -= 1
print(total)
