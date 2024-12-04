import re

f = open("input.txt")

count = 0

while line := f.readline():
    tokens = re.split(r"\s+", line.strip())
    nums = list(map(int, tokens))

    prev = None
    valid = True
    prev_move = None
    for num in nums:
        if prev is None:
            prev = num
            continue
        
        move = prev > num
        if prev_move is None:
            prev_move = move
        else:
            if prev_move != move:
                valid = False
                break

        if abs(prev - num) < 1 or 3 < abs(prev - num):
            valid = False
            break
        
        prev = num

    if valid:
        count += 1
    
    print(valid, tokens)

print(count)
    