import string
import torch

ascii_letters = [" "] + list(string.ascii_uppercase)
lines = []

def encode(letters):
    x = [
        [ascii_letters.index(c) for c in line]
        for line in letters
    ]
    return torch.tensor(x, dtype=torch.float32)[None, None, ...]

kernel_1 = encode([["M", " ", "M"], [" ", "A", " "], ["S", " ", "S"]])
kernel_2 = encode([["S", " ", "M"], [" ", "A", " "], ["S", " ", "M"]])
kernel_3 = encode([["S", " ", "S"], [" ", "A", " "], ["M", " ", "M"]])
kernel_4 = encode([["M", " ", "S"], [" ", "A", " "], ["M", " ", "S"]])

kernels = [
    kernel_1, kernel_2, kernel_3, kernel_4
]

with open("input.txt") as f:
    while line := f.readline():
        lines.append(
            [ascii_letters.index(c) for c in list(line.strip())]
        )

target = (kernel_1.squeeze() * kernel_1.squeeze()).sum()
matrix = torch.tensor(lines, dtype=torch.float32)[None, None, ...]

res = sum([
    (torch.nn.functional.conv2d(matrix, kernel) == target).sum()
    for kernel in kernels
])

print(res)
