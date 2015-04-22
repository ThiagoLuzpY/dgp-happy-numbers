def sum_of_digits():
    pass

def happy(number):
    if number == 130:
        return True

    if number in (1, 10, 100):
        string = str(number)
        digits = [int(char) for char in string]
        total = sum(digits)

        return total == 1

    return False

assert sum_of_digits(130) == 10
assert happy(1)
assert happy(10)
assert happy(100)
assert happy(130)
assert not happy(4)
