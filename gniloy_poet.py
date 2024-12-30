from random import randint

# сущ прил гл сущ
noun = ["тыква", "привидение", "конфеты","костюмы", "гарри портер"]
verb = ["ходить", "ездить", "чинить"]
adjective = ["тыквенный", "страшный"]

count = int(input("Кол-во четверостиший"))

for i in range(count):
        print(noun[randint(0, len(noun) - 1)], adjective[randint(0, len(adjective) - 1)], verb[randint(0, len(verb) - 1)], noun[randint(0, len(noun) - 1)])