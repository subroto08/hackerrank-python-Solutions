from itertools import permutations

s, k = input().split()
k = int(k)
result = permutations(sorted(s), k)

for i in result:
  print("".join(i))