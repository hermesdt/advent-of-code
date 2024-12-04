import string
import torch
import numpy as np

ascii_letters = [" "] + list(string.ascii_uppercase)
lines = []

def encode(letters):
    x = [
        [ascii_letters.index(c) for c in line]
        for line in letters
    ]
    return torch.tensor(x, dtype=torch.float32)[None, None, ...]

horizontal = encode([["X", "M", "A", "S"]])
horizontal_rev = encode([["S", "A", "M", "X"]])
vertical = encode([["X"], ["M"], ["A"], ["S"]])
vertical_rev = encode([["S"], ["A"], ["M"], ["X"]])
diagonal_1 = encode([["X", " ", " ", " "], [" ", "M", " ", " "], [" ", " ", "A", " "], [" ", " ", " ", "S"]])
diagonal_1_rev = encode([["S", " ", " ", " "], [" ", "A", " ", " "], [" ", " ", "M", " "], [" ", " ", " ", "X"]])
diagonal_2 = encode([[" ", " ", " ", "X"], [" ", " ", "M", " "], [" ", "A", " ", " "], ["S", " ", " ", " "]])
diagonal_2_rev = encode([[" ", " ", " ", "S"], [" ", " ", "A", " "], [" ", "M", " ", " "], ["X", " ", " ", " "]])

kernels = [
    horizontal, horizontal_rev,
    vertical, vertical_rev,
    diagonal_1, diagonal_1_rev,
    diagonal_2, diagonal_2_rev
]

with open("input.txt") as f:
    while line := f.readline():
        lines.append(
            [ascii_letters.index(c) for c in list(line.strip())]
        )

target = horizontal.squeeze() @ horizontal.squeeze()
matrix = torch.tensor(lines, dtype=torch.float32)[None, None, ...]

res = sum([
    (torch.nn.functional.conv2d(matrix, kernel) == target).sum()
    for kernel in kernels
])

print(res)
