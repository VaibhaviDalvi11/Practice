n = 5
for i in range(1, n + 1):
    # (n - i) spaces followed by (2 * i - 1) stars
    print(" " * (n - i) + "*" * (2 * i - 1))