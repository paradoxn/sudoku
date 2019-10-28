import numpy as np

sudolist = [
[0,0,0,3,0,7,4,0,0],
[9,0,0,0,0,4,0,0,8],
[3,7,0,0,0,0,0,6,0],
[8,2,0,9,0,0,6,0,0],
[0,0,1,2,0,0,9,0,4],
[0,4,0,0,3,8,0,5,0],
[2,0,8,6,9,0,7,0,0],
[0,9,0,0,0,0,0,0,0],
[7,5,0,0,0,0,0,0,6]
]

sudo = np.array(sudolist)


def judgeSudoku(i, j, array):
    lists = []
    a = i // 3 * 3
    b = j // 3 * 3
    row = array[i, :]
    column = array[:, j]
    nightarea = array[a:a + 3, b:b + 3]
    for num in range(1, 10):
        if num not in row and num not in column and num not in nightarea:
            lists.append(num)
    return lists

def main(array):
    while True:
        countss=0
        everyposslist = []
        for i in range(0, 9):
            posslist = []
            for j in range(0, 9):
                num = array[i, j]
                if num != 0:
                    posslist.append([num])
                else:
                    posslist.append(judgeSudoku(i, j, array))
            everyposslist.append(posslist)
        arrayx = np.array(everyposslist)
        for n in range(0, 9):
            for m in range(0, 9):
                if array[n, m] == 0:
                    LL = arrayx[n, m]
                    for num2 in LL:
                        a = n // 3 * 3
                        b = m // 3 * 3
                        rowstr = str(arrayx[n, :])
                        columnstr = str(arrayx[:, m])
                        nightareastr = str(arrayx[a:a + 3, b:b + 3])
                        num2=str(num2)
                        if rowstr.count(num2) == 1 or columnstr.count(num2) == 1 or nightareastr.count(num2) == 1:
                            print('%s行%s列单元格有可推理填入,值%s' % (n, m, num2))
                            array[n, m] = num2
                            countss += 1
                            break

        if countss==0:
            break
    if 0 not in array:
        print('已结束，最终结果为\n',array)
    else:
        print("未完成,目前取得进展\n", arrayx)




if __name__ == '__main__':
    result = main(sudo)