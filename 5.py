arr = list(set(map(int, input().split()))) # Use set to remove duplicates
arr.sort()
print(arr[-2] if len(arr) > 1 else "No second largest")