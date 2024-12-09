#!/usr/bin/env python3

import re

import numpy as np

search_word = "XMAS"
input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def multi_direction_word_count(word: str, input: str) -> int:
    # Clean input and convert to matrix
    lines = [line for line in input.strip().split("\n")]
    matrix = np.array([list(line) for line in lines])

    # Get horizontal matches (forward and backward)
    horizontal_text = "\n".join(lines)
    forward_pattern = rf"{word}"
    backward_pattern = rf"{word[::-1]}"
    horizontal_matches = len(list(re.finditer(forward_pattern, horizontal_text))) + len(
        list(re.finditer(backward_pattern, horizontal_text))
    )

    # Get vertical matches by rotating matrix
    vertical_text = "\n".join(["".join(row) for row in matrix.T])
    vertical_matches = len(list(re.finditer(forward_pattern, vertical_text))) + len(
        list(re.finditer(backward_pattern, vertical_text))
    )

    return horizontal_matches + vertical_matches


print(multi_direction_word_count(search_word, input))
