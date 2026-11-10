def sum_digits(number):
        result = abs(number) + str(number)
        return result
    
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')