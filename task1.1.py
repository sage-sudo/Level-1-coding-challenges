def multiples_of_3_or_5(number):
    number = int(number)

    store_multiples = list()
    for multiple in range(1, number):
        if multiple % 3 == 0 or multiple % 5 == 0:
            store_multiples.append(multiple)

    #   print(store_multiples)

    summed = store_multiples[0]
    for integer in range(1, len(store_multiples)):
        #   print(store_multiples[integer])
        summed += store_multiples[integer]

    print(f"The sum of all the multiples of 3 or 5 below {number} is: {summed}")


multiples_of_3_or_5(1000)