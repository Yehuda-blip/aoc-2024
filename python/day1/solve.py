from collections import Counter
import itertools
from typing import Iterator


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


def parse(line: str) -> tuple[int, int]:
    a, b = line.split()
    return int(a), int(b)


def lists(data: Iterator[tuple[int, int]]) -> tuple[list[int], list[int]]:
    data1, data2 = itertools.tee(data)
    data1, data2 = map(lambda r: r[0], data1), map(lambda r: r[1], data2)
    return sorted(data1), sorted(data2)


def solve_a(text: str) -> int:
    data1, data2 = lists(map(parse, text.splitlines()))
    data = zip(data1, data2)
    result = sum(map(lambda row: abs(row[0] - row[1]), data))
    return result


print(f"{solve_a(EXAMPLE)=}, {solve_a(INPUT)=}")


def solve_b(text: str) -> int:
    data1, data2 = lists(map(parse, text.splitlines()))
    count = Counter(data2)
    return sum(count[v] * v for v in data1)


print(f"{solve_b(EXAMPLE)=}, {solve_b(INPUT)=}")
