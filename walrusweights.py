
def main():
    n = int(input())
    nsort = sorted(map(int, (input() for _ in range(n))))
    content = set()
    content.add(0)
    weight = 0
    maximum = 1000
    for i in nsort:
        for j in list(content):
            diff = abs(1000 - (i + j))
            if diff == maximum and weight < (i + j):
                weight = (i + j)
            elif diff < maximum:
                weight = (i + j)
                maximum = diff
            if diff > maximum and (i + j) > 1000:
                continue
            content.add(i+j)
    print(weight)

main()
