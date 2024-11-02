def convert_to_decimal(n, S):
    decimal_value = 0
    length = len(n)
    
    for i in range(length):
        char = n[i]
        
        if '0' <= char <= '9':
            value = int(char)
        elif 'A' <= char <= 'Z':
            value = ord(char) - ord('A') + 10
        else:
            raise ValueError("Неверный символ в числе.")
        
        if value >= S:
            raise ValueError(f"Значение {char} превышает основание системы {S}.")
        
        decimal_value += value * (S ** (length - 1 - i))
    
    return decimal_value

n = input("Введите число (в системе счисления S): ")
S = int(input("Введите основание системы счисления S: "))

try:
    decimal_value = convert_to_decimal(n, S)
    print(f"Число {n} в системе счисления {S} в десятичной системе: {decimal_value}")
except ValueError as e:
    print(e)
