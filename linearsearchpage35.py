def linear_search(L, x):
    n = len(L)
    i = 0
    while i < n:
        if L[i] == x:
            return i
        i += 1
    i = -1
    return i


if __name__ == "__main__":
    L = ['Babli', 'Hajar Bochor Dhore', '3', 2]
    print(linear_search(L, "Hajar Bochor Dhore"))
