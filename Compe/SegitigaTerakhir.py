import sys
input = lambda: sys.stdin.readline().strip()

#  __
#<(o )___
# ( ._> /
#  `---'

def solve():
    x, y, z = map(int, input().split())
    if (2**z) + (2**y) == 2**x:
        print('Ya')
    else:
        print('Tidak')

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()