import re
from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

count = 0

def is_valid_pair(a, b, c=None):
    if abs(a - b) == 0: return False
    if abs(a - b) > 3: return False

    if c is not None:
        if (a > b) != (b > c):
            return False
    
    return True


while line := f.readline():
    tokens = re.split(r"\s+", line.strip())
    nums = list(map(int, tokens))

    fixed = False
    valid = True
    
    i = 0
    while i < len(nums):
        if i == 0:
            i += 1
            continue

        a, b = nums[i], nums[i - 1]

        c = None
        if i >= 2 and len(nums) >= 3:
            c = nums[i - 2]
        
        if not is_valid_pair(a, b, c):
            if fixed:
                valid = False
                break
            else:
                fixed = True
                nums.pop(i - 1)
                continue

        i += 1

    if valid:
        count += 1
    
    print(valid, tokens)

print(count)
    