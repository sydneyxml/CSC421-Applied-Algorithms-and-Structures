

def MSS(array):
    end = curr = array[0]

    for i in array[1:]:
        end = max(i, end + i)
        curr = max(curr, end)
    return curr


split = int(input().split()[1])

print(MSS(list(map(lambda z: int(z) - split, input().split()))))
