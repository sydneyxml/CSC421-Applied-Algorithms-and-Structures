import sys

def main():
  n,m = map(int, sys.stdin.readline().split())
  checks = []
  for line in sys.stdin:
    a,b = map(lambda x: int(x) - 1, line.split())
    checks.append(1<<a | 1<<b)

  count = 1<<n
  for i in xrange(1<<n):
    for c in checks:
      if c & i == c:
        count -= 1
        break
  print count

if __name__ == '__main__':
  main()
