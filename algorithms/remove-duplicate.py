original_names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]


def remove_duplicates(original_list):
    new_list = []
    for name in original_list:
        if name not in new_list:
            new_list.append(name)
    return new_list


print(remove_duplicates(original_names))
