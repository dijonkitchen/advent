import re
from turtle import backward

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
    forward_pattern = rf"{word}"
    forward_matches = len(list(re.finditer(forward_pattern, input)))

    backward_pattern = rf"{word[::-1]}"
    backward_matches = len(list(re.finditer(backward_pattern, input)))

    return forward_matches + backward_matches


print(multi_direction_word_count(search_word, input))
