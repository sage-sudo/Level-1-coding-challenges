def finding_65(num1, num2):
    find = 65
    number1 = int(num1)
    number2 = int(num2)

    store_numbers = [number1, number2]
    if store_numbers[0] + store_numbers[1] == find:
        return "true"

    elif store_numbers[0] == find or store_numbers[1] == find:
        return "true"

    else:
        return "false"


found = finding_65(30, 35)
print(found)
