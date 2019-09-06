number_list = [13,2,54,3,23]
min = number_list[0]

for num in range(0,len(number_list)):
    if number_list[num] < min:
        min = number_list[num]

print(min)
