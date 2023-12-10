n = int(input())

citizen = list(map(int, input().split()))
citizen.sort()
maxx = citizen[-1]

spent = 0

for welfare in citizen:
    spent += maxx - welfare

print(spent)
