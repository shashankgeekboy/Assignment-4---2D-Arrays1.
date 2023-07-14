def arrangeCoins(n):
    complete_rows = 0
    k = 1

    while (k * (k + 1)) // 2 <= n:
        complete_rows += 1
        k += 1

    return complete_rows
