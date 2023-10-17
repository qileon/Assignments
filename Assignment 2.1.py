def calculate_sum():
    while True:
        input_str = input("Enter three numbers. (or 0 to exit): ")
        nums = input_str.split()
        
        if '0' in nums:
            break
        
        if len(nums) != 3:
            print("THREE NUMBERS!")
            continue

        num1, num2, num3 = map(float, nums)

        total = num1 + num2 + num3

        if num1 == num2 == num3:
            result = total * 3
            print(f"The power of the three numbers is {result}")
        else:
            print(f"The sum of the three numbers is {total}")

calculate_sum()