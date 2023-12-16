length = int(input())
occ_count = {}
food_items = input()
count_L = food_items.count("L")
count_O = food_items.count("O")

for i in range(1, length):
    part_L = food_items[:i].count("L")
    part_O = food_items[:i].count("O")
    remaing_L = count_L - part_L
    remaing_O = count_O - part_O

    if (part_L != 0 or part_O != 0) and (remaing_L != part_L and remaing_O != part_O):
        print(i)
        break
else:
    print(-1)
