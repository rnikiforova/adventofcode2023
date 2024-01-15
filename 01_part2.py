import re

num_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
pattern = re.compile(r"(?=(three|seven|eight|four|five|nine|one|two|six|\d))")


def digits_per_line(line):
    matches = list(map(lambda x: x.group(1), pattern.finditer(line)))
    if matches:
        left, right = matches[0], matches[-1]
        return num_map.get(left, left), num_map.get(right, right)
    return ""


def reg(path):
    with open(path) as f:
        return sum(int("".join(digits_per_line(line))) for line in f)


if __name__ == "__main__":
    assert digits_per_line("9onekptdkglrnloneightfr") == ("9", "8")
    assert reg("data/01_calibration_letters.txt") == 281
