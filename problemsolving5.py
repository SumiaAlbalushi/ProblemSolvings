def gcd(a, b):

    while b:

        a, b = b, a % b

    return a


def count_fractions_pairs(numerator, denominator):

    n = len(numerator)

    count = 0


    for i in range(n):

        for j in range(i + 1, n):

            num1, num2 = numerator[i], numerator[j]

            den1, den2 = denominator[i], denominator[j]


            # Check if fractions sum up to 1

            if num1 * den2 + num2 * den1 == den1 * den2:

                count += 1


    return count


N = 4

numerator = [1, 2, 2, 8]

denominator = [2, 4, 6, 12]

output = count_fractions_pairs(numerator, denominator)

print("Count of pairs with sum equal to 1:", output)