from collections import Counter
import itertools
from typing import Iterator

import numpy as np


EXAMPLE = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


with open("inputs\day1.txt", 'r') as text:
    INPUT = text.read()


def parse(text: str) -> np.ndarray[int]:
    parseline = lambda line: list(map(int, line.split()))
    return np.array(list(map(parseline, text.splitlines())))


def solve_a(text: str) -> int:
    data1, data2 = np.sort(parse(text).T)
    return int(np.sum(np.abs(data1 - data2)))


print(f"{solve_a(EXAMPLE)=}, {solve_a(INPUT)=}")


def solve_b(text: str) -> int:
    data1, data2 = parse(text).T
    count = Counter(data2)
    return int(sum(count[v] * v for v in data1))


print(f"{solve_b(EXAMPLE)=}, {solve_b(INPUT)=}")
