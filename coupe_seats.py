seat = int(input())
lst = ["W","M","A","A","M","W","W","M","A","A","M","W",]

count = list(range(1, 12, 2))
for i in range(seat):
    b = lst[i%12]
    if seat % 12<= 6:
        another_seat = seat + count[(seat%6)-1]
    if seat % 12 > 6:
        count.reverse()
        another_seat = seat - count[(seat%6)-1]
print(f"{another_seat}{b}")
