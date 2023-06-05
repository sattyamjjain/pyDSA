import timeit


# Function to calculate the sum of a list of numbers
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Measure the execution time using timeit
def measure_time():
    setup_code = '''
        from __main__ import sum_numbers
        numbers = [1, 2, 3, 4, 5]
        '''
    stmt = 'sum_numbers(numbers)'
    time_taken = timeit.timeit(stmt, setup=setup_code, number=100000)
    print("Execution time:", time_taken)


# Run the measurement function
measure_time()
