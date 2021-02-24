k1,k2,k3,k4 = list(map(int, input().split()))
tot = 0

k1,k3,k4 = k1-min256, k3-min256, k4-min256
min32 = min(k1,k2)

k1,k2 = k1-min32, k2-min32
tot = 256*min256 + 32*min32

print(tot)
