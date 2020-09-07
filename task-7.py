def view_matrix(n):
    dx, dy = 1, 0
    x, y = 0, 0
    matrix = [[None] * n for _ in range(n)]
    for i in range(1, n ** 2 + 1):
        matrix[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not matrix[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    for x in list(zip(*matrix)):
        print(*x)


while True:
    user_input = input("Enter int value: ")
    try:
        n = int(user_input)
        break
    except ValueError:
        print("Not an int value!")

view_matrix(n)

