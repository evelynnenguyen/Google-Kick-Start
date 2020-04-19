t = input("Please input the number of test cases: ")
for i in range(t):
    a, b = [int(x) for x in input("Enter the exclusive lower bound and the inclusive upper bound: ").split()]
    n = input("Enter the maximum number of guesses: ")
    for j in range(n):
        q = input("Enter your guess: ")
        