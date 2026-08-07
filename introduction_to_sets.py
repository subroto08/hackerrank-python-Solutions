def average(array):
  unique = set(array)
  average = sum(unique)/len(unique)
  return average


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)