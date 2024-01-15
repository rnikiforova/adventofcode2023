from timeit import Timer


def two_sides(path):
    with open(path) as f:
        total = 0
        for line in f:
            curr_line = line.rstrip()
            right = len(curr_line) - 1
            left_digit = None
            right_digit = None
            for letter in curr_line:
                right_letter = curr_line[right]
                if not left_digit and letter.isdigit():
                    left_digit = letter
                if not right_digit and right_letter.isdigit():
                    right_digit = right_letter
                else:
                    right -= 1
                if left_digit and right_digit:
                    break

            if right_digit is None:
                right_digit = left_digit
            if left_digit and right_digit:
                curr_sum = int(left_digit + right_digit)
                total += curr_sum
        return total


def naive(path):
    with open(path) as f:
        total = 0
        for line in f.readlines():
            line_num = "".join(
                [
                    next(filter(str.isdigit, line), ""),
                    next(filter(str.isdigit, reversed(line)), ""),
                ]
            )
            total += int(line_num or 0)
        return total


if __name__ == "__main__":
    path = "data/01_calibration_example.txt"
    assert naive(path) == 142
    assert two_sides(path) == 142

    path = "data/01_calibration_extended.txt"
    assert naive(path) == 195
    assert two_sides(path) == 195

    print("Start timing..")
    n = 70000
    print("naive    ", Timer(stmt=lambda: naive(path)).timeit(n))
    print("two_sides", Timer(stmt=lambda: two_sides(path)).timeit(n))
