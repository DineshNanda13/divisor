def divisors(n):
    answers = []
    for x in range(1, n + 1):
        if n % x == 0:
            answers.append(x)

    return answers

print(divisors(15))

'''
example:
6 -> [1, 2, 3, 6]
9 -> [1, 3, 9]
101 -> [1, 101]
'''
