game_map = [["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]

cur_pl = 0
i=0

win = False;


def pr_map(gm):
    s = " "
    for i in range(len(gm[0])):
        s += str(i)
    print(s)

    for i in range(len(gm)):
        s = str(i)
        for j in range(len(gm[i])):
            s += gm[i][j]
        print(s)


def check(gm, cl):
    c = 0
    for i in range(len(gm)):
        c = 0
        for j in range(len(gm[i])):
            if gm[i][j] == cl:
                c += 1
        if c == 3:
            print(cl+" - победили")
            return True

    for j in range(len(gm[0])):
        c = 0
        for i in range(len(gm)):
            if gm[i][j] == cl:
                c += 1
        if c == 3:
            print(cl+" - победили")
            return True
        
    c = 0
    for i in range(len(gm)):
        if gm[i][i] == cl:
            c += 1
    if c == 3:
        print(cl+" - победили")
        return True
    c = 0
    
    for i in range(len(gm)-1, -1, -1):
        if gm[i][i] == cl:
            c += 1
    if c == 3:
        print(cl+" - победили")
        return True
    


pr_map(game_map)

while i<9 and not win:
    cell_n = ""

    if cur_pl == 0:
        cell_n = input("Игрок 1, введите номер клетки(xy)")
        if game_map[int(cell_n[1])][int(cell_n[0])] == "-":
            game_map[int(cell_n[1])][int(cell_n[0])] = "x"
            cur_pl = 1
            pr_map(game_map)
            win = check(game_map, "x")
        else:
            pr_map(game_map)
            print("!!!!ОШИБКА - эта клетка уже занята!!!!")
    else:
        cell_n = input("Игрок 2, введите номер клетки(xy)")
        if game_map[int(cell_n[1])][int(cell_n[0])] == "-":
            game_map[int(cell_n[1])][int(cell_n[0])] = "o"
            cur_pl = 0
            pr_map(game_map)
            win = check(game_map, "o")
        else:
            pr_map(game_map)
            print("!!!!ОШИБКА - эта клетка уже занята!!!!")

print("игра окончена")


    


