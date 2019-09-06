number_list = [0, 1, 2, 3, 5, 7, 6, 8, 9]


def missing_number(numbers):
    numbers_len = len(numbers)

    length_total = (numbers_len * (numbers_len + 1))/2

    sum_of_numbers = sum(numbers)

    return length_total - sum_of_numbers


print(missing_number(number_list))
