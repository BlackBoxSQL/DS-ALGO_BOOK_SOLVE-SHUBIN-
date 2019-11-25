def avarage(numbers):
    if not numbers:
        return None
    return sum(numbers)/len(numbers)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    desired_result = 3.0
    result = avarage(numbers)
    if desired_result == result:
        print("test passed!")
    else:
        print("Test failed!", "received :", result,
              "expected :", desired_result)
