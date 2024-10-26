def decimal_to_hexadecimal(decimal_number):
    if decimal_number < 0:
        return "Негативные числа не поддерживаются"
    hex_number = hex(decimal_number)
    return hex_number[2:] 

decimal_input = int(input("Введите десятичное число: "))
hex_output = decimal_to_hexadecimal(decimal_input)
print(f'Шестнадцатеричное число: {hex_output}')