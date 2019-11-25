def avarage(numbers):
    if not numbers:
        return None
    return sum(numbers)/len(numbers)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(avarage(numbers))
