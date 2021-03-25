op = ['+', '-', '*', '//']
d = {}
for op1 in op:
    for op2 in op:
        for op3 in op:
            f = f'4 {op1} 4 {op2} 4 {op3} 4'
            d[eval(f)] = f

m = int(input())

for i in range(m):
    n = int(input())
    if n in d:
        print(d.get(n).replace('//', '/'), '= ', n)
    else:
        print('no solution')
