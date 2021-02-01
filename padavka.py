def сollatz_conjecture(input_number, count=0):
    if input_number != 1:
        if input_number % 2 == 0:
            input_number = input_number / 2
            return сollatz_conjecture(input_number, count+1)
        else:
            input_number = input_number * 3 + 1
            return сollatz_conjecture(input_number, count+1)
    else:
        return input_number, count
print(сollatz_conjecture(9))
print(сollatz_conjecture(10))
print(сollatz_conjecture(37))
print(сollatz_conjecture(5))