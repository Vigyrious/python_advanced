rows, columns = map(int, input().split(", "))
matrix = []
[matrix.append([int(i) for i in input().split(", ")]) for k in range(rows)]
largest_submaze = []
largest_sum = 0
for i in range(rows-1):
    for k in range(columns-1):
        maze_sum = 0
        top_row = i
        bottom_row = i+1
        right_top = k
        right_bottom = k+1
        maze = [[matrix[top_row][right_top],matrix[top_row][right_bottom]],[matrix[bottom_row][right_top],matrix[bottom_row][right_bottom]]]
        for submaze in maze:
            for num in submaze:
                maze_sum += int(num)
        if maze_sum > largest_sum:
            largest_sum = maze_sum
            largest_submaze = maze
for submaze in largest_submaze:
    print(*submaze)
print(largest_sum)