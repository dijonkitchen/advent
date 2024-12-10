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

def get_diagonals(matrix):
    diags = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1, -matrix.shape[0], -1))
    return [''.join(n) for n in diags]

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

    # Get diagonal matches
    diagonals = get_diagonals(matrix)
    diagonal_text = "\n".join(diagonals)
    diagonal_matches = len(list(re.finditer(forward_pattern, diagonal_text))) + len(
        list(re.finditer(backward_pattern, diagonal_text))
    )

    return horizontal_matches + vertical_matches + diagonal_matches


print(multi_direction_word_count(search_word, input))
