import sys

def fibo(num):
    num1 = 0
    num2 = 1


    for _ in range(0, num):
        num_to_change = num1 + num2
        num2 = num1
        num1 = num_to_change
        print(num2)


def main():
    number = int(sys.argv[1
    fibo(number)

if __name__ == "__main__":
    main()
