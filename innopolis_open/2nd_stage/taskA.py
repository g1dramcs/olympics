import math

def min_unused_area(a, b, k):
    if b > a:
        a, b = b, a
    
    min_unused = float('inf')

    for x in range(1, k + 1):
        tile_width = a / x
        tile_height = b / x

        tiles_x = math.ceil(a / tile_width)
        tiles_y = math.ceil(a / tile_height)
        tiles_needed = tiles_x * tiles_y
        
        used_area = tiles_needed * (tile_width * tile_height)

        total_area = a * a

        unused_area_wo_cuts = used_area - total_area

     
        min_unused_with_cuts = float('inf')
        for r in range(1, math.ceil(tile_height)):
            part1 = tile_width * r
            part2 = tile_width * (tile_height - r)

        
            if part1 >= a or part2 >= a:
                continue
            
        
            unused_area_with_cuts = used_area - total_area
            
         
            min_unused_with_cuts = min(min_unused_with_cuts, unused_area_with_cuts)

        min_unused = min(min_unused, unused_area_wo_cuts, min_unused_with_cuts)


    return int(min_unused)


a = int(input())
b = int(input())
k = int(input())

print(min_unused_area(a, b, k))
