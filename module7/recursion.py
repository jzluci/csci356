import timeit


# Define the functions
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def reverse_list(lst):
    # Base case: if the list is empty or has only one element, return it as is
    if len(lst) <= 1:
        return lst
    # Recursive case: reverse the rest of the list and append the first element at the end
    return reverse_list(lst[1:]) + [lst[0]]


# Define the timeit setup
setup_code = '''
from __main__ import fibonacci_recursive, fibonacci_iterative
'''


# Measure and print time taken for each function
def measure_time():
    for n in [10, 15, 20]:
        print(f"n = {n}:")
        # Time recursive version
        recursive_time = timeit.timeit(f'fibonacci_recursive({n})', setup=setup_code, number=1000) * 1000
        print(f"  Recursive time: {recursive_time:.6f} ms")

        # Time iterative version
        iterative_time = timeit.timeit(f'fibonacci_iterative({n})', setup=setup_code, number=1000) * 1000
        print(f"  Iterative time: {iterative_time:.6f} ms")


def binary_search_recursive(arr, target, start, end):
    # Base case: if the start index exceeds the end index, the target is not found
    if start > end:
        return -1

    # Calculate the middle index
    mid = len(arr) // 2

    # Check if the target is present at mid
    if arr[mid] == target:
        return mid
    # If the target is smaller, search in the left sublist
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, start, mid - 1)
    # If the target is larger, search in the right sublist
    else:
        return binary_search_recursive(arr, target, mid + 1, end)


def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)


def main():
    measure_time()
    original_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(original_list)
    print(f"Reversed list: {reversed_list}")  # Output: [5, 4, 3, 2, 1]
    sorted_list = [1, 3, 4, 5, 7, 9, 10]
    target = 5
    result = binary_search(sorted_list, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")


if __name__ == '__main__':
    main()
