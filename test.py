def minimum_time_to_home(x, y, w, s):
    time_straight = (x + y) * w
    diag_moves = min(x, y)
    straight_moves = abs(x - y)
    time_mixed = diag_moves * s + straight_moves * w
    
    return min(time_straight, time_mixed)

x, y, w, s = map(int, input().split())
print(minimum_time_to_home(x, y, w, s))
