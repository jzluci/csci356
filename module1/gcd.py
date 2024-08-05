def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def main():
    #read input
    input_nums = input("Please input two integers: ")

    #split input
    num1, num2 = map(int, input_nums.split())

    #gcd
    result = gcd(num1, num2)

    #print
    print(f"The GCD between {num1} and {num2} is: {result}.")

if __name__ == "__main__":
    main()