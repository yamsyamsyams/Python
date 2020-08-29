def collatz(number):
    if number % 2 == 0:
        print(number)
        return number
    elif number % 2 == 1:
        print(number + 1)
        return number
    while number != 1:
        collatz()

if __name__ == '__main__':
    print("Enter number: ")
    userIn = int(input())
    collatz(userIn)