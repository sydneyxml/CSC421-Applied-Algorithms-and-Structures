
def woodcutting(l):
    result = 0
    t = 0
    for x in l:
        t += x
        result += t
    return result / len(l)


for _ in range(int(input())):
    print('%.6f' % woodcutting(sorted(sum(map(int, input().split()[1:])) for _ in range(int(input())))))
