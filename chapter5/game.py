def draw(p):
    print(f"{p[0]}  | {p[1]}  | {p[2]}")
    print("---+----+---")
    print(f"{p[3]}  | {p[4]}  | {p[5]}")
    print("---+----+---")
    print(f"{p[6]}  | {p[7]}  | {p[8]}")


def win(p):
    winList = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
               [1, 4, 7], [2, 5, 8], [0, 4, 5], [2, 4, 6]]

    for item in winList:
        if equal(p[item[0]], p[item[1]], p[item[2]]):
            return True


def equal(a, b, c):
    if a == b == c:
        return True
    else:
        return False


def check_list(arr):
    return all(isinstance(item, str) for item in arr)


arr = []
for i in range(9):
    arr.append(i+1)

draw(arr)
flag = False
stamp = True

while not flag:
    try:
        position = int(input("enter 1~9: "))
    except ValueError:
        print("Enter an integer!")
        continue

    if position in arr:
        if stamp:
            arr[position-1] = 'O'
            stamp = False
        else:
            arr[position-1] = 'X'
            stamp = True
    else:
        print(f'{position} already choose!!')

    draw(arr)
    if win(arr):
        flag = True
        if stamp:
            print("X WIN")
        else:
            print("O WIN")
    else:
        if check_list(arr):
            print("NO WINNER")
            break
