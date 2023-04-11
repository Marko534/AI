def add(stat):
    for i in range(len(stat)):
        stat[i] *= 2
    return 1


if __name__ == '__main__':
    test = [0] * 10

    n = int(input())
    l = int(input())

    disc = [0] * l
    for i in range(n):
        disc[i] = i + 1

    print(disc)
    print(disc.index(3))