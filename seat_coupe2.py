def get_seat_type(r):
    if r == 0 or r == 5:
        return 'W'
    elif r == 1 or r == 4:
        return 'M'
    else:
        return 'A'

def calculate_seat(n):
    if n <= 48:
        r = (n - 1) // 8
    else:
        r = (n - 1) // 10

    seat_type = get_seat_type(r)
    opposite_seat = n + (-1) ** (n % 2 + 1)
    
    return opposite_seat, seat_type


n = int(input())
opposite_seat, seat_type = calculate_seat(n)
print(opposite_seat, seat_type)
