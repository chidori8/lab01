import test

def evklid(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

if __name__ == "__main__":
    print(evklid(50, 10))

    if evklid(50, 10) == test.NOD(50, 10):
        print("тест прошёл успешно")
    else:
        print("тест не прошёл")