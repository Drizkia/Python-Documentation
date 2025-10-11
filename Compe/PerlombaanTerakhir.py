import sys
input = lambda: sys.stdin.readline().strip()

#  __
#<(o )___
# ( ._> /
#  `---'

def solve():
    s = input().upper()
    if s.count('O') == 1:
        print('Ya')
    else:
        print("Tidak")

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()