id_num = 20230285
digits = str(id_num)

for i in range(len(digits)):
    digit1 = int(digits[i])
    if i > 0:
        digit2 = int(digits[i-1])
    else:
        digit2 = 0
    sum_digits = digit1 + digit2
    sub_digits = digit1 - digit2
    mult_digits = digit1 * digit2

    print("Sum: ", sum_digits)
    print("Subtraction: ", sub_digits)
    print("Multiplication: ", mult_digits)