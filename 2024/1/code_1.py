import re

f = open("input.txt")

left = []
right = []

while line := f.readline():
    tokens = re.split(r"\s+", line.strip())
    a,b = list(map(int, tokens))

    if len(left) == 0:
        left.append(a)
        right.append(b)
        continue

    for i in range(len(left)):
        if a is not None:
            if left[i] > a:
                left.insert(i, a)
                a = None
        
        if b is not None:
            if right[i] > b:
                right.insert(i, b)
                b = None
        
        if (a, b) == (None, None): break
    
    if a is not None: left.append(a)
    if b is not None: right.append(b)


result = 0
for i in range(len(left)):
    result += abs(left[i] - right[i])

print(result)
