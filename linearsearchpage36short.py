def linear_search(L, x):
    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i
    return -1


if __name__ == "__main__":
    L = ['Babli', 'Hajar Bochor Dhore', '3', 2]
    print(linear_search(L, "Babli"))
