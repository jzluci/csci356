import timeit

from StackADT import *


def rev_string_A(my_string):
    s = StackA()
    for char in my_string:
        s.push(char)

    reverse = ''
    while not s.is_empty():
        reverse += s.pop()


def rev_string_B(my_string):
    s = StackB()
    for char in my_string:
        s.push(char)

    reverse = ''
    while not s.is_empty():
        reverse = s.pop() + reverse


def main():
    # Generate a test string of at least 1000 characters
    test_string = 'a' * 1000

    # Measure the time for rev_string_A
    time_A = timeit.timeit(lambda: rev_string_A(test_string), number=1000) * 1000
    print(f"Time for rev_string_A: {time_A:.6f} ms")

    # Measure the time for rev_string_B
    time_B = timeit.timeit(lambda: rev_string_B(test_string), number=1000) * 1000
    print(f"Time for rev_string_B: {time_B:.6f} ms")

    x = 0
    x = x + \
        1


if __name__ == '__main__':
    main()
