def add(stat):
    for i in range(len(stat)):
        stat[i] *= 2
    return 1


if __name__ == '__main__':
    stat = ((1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16))
    temp = 100, 1000
    x = max(abs(temp[0]+y[1]) for y in stat)
    print(temp)
