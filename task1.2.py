def finding_3(num1, num2):
    find = 3
    number_1 = int(num1)
    number_2 = int(num2)

    store_numbers = [number_1, number_2]
    for check in store_numbers:
        if check == find:
            sum_of = store_numbers[0] + store_numbers[1]
            if str(find) in str(sum_of):
                return "true"

        else:
            return "false"


found_3 = finding_3(3, 33)

print(found_3)
