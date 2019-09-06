number_list = [13,2,54,3,23]
max = number_list[0]

for num in range(0,len(number_list)):
    if number_list[num] > max:
        max = number_list[num]

print(max)
