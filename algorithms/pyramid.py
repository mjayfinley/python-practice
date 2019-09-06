userInput = int(input("Enter the number of rows: "))
row = 0

#outer loop for number of rows and number of spaces
while(row < userInput):
    row += 1
    spaces = userInput - row

    #inner loop to print a space while space counter is less than number
    #of spaces, for both side of pyramid?
    spaces_counter = 0
    while(spaces_counter < spaces):
        print(" ", end='')
        spaces_counter += 1

    #inner loop to print * at each row given the equation and remaining rows
    num_astrisks = 2*row - 1
    while(num_astrisks > 0):
        print("*", end='')
        num_astrisks -= 1

    print()
