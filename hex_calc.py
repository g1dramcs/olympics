def decimal_to_hexadecimal(decimal_number):
    if decimal_number < 0:
        return "Ошибка: число должно быть неотрицательным"
    
    hex_digits = []
    
    hex_chars = "0123456789ABCDEF"
    if decimal_number == 0:
        return "0"

    while decimal_number > 0:
        remainder = decimal_number % 16  
        hex_digits.append(hex_chars[remainder]) 
        decimal_number //= 16 
    
    hex_digits.reverse()
    return ''.join(hex_digits)

num_system = int(input("Введите систему счисления"))
decimal_input = int(input("Десятичное число: "))
hex_output = decimal_to_hexadecimal(decimal_input)
print(f'Шеснадцатиричное число: {hex_output}')