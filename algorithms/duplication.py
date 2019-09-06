numbers = [1, 2, 3, 4, 5]


def duplicate_numbers(number_array):
    numbers_duplicated = []

    while len(numbers_duplicated) < (len(number_array) * 2):
        for number in number_array:
            numbers_duplicated.append(number)

    return numbers_duplicated


print(duplicate_numbers(numbers))
