import re

f = open("input.txt")

left = []
right = {}

while line := f.readline():
    tokens = re.split(r"\s+", line.strip())
    a,b = list(map(int, tokens))

    left.append(a)

    if b not in right:
        right[b] = 1
    else:
        right[b] += 1
    
result = 0
for n in left:
    result += n * right.get(n, 0)

print(result)