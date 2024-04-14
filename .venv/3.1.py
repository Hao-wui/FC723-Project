class EuclideanAlgorithm:
    def gcd(self, a, b):
        """
1.Write two integers as a and b.
2.If b is equal to 0, then a is the greatest common divisor of two integers.
3.Otherwise, calculate the remainder of a divided by b, denoted as r.
4.Update the value of b to the original r, and update the value of a to the original b.
        """
        while b != 0:
            remainder = a % b#By repeatedly taking the remainder operation,
            # the problem of two integers is transformed into the problem of smaller integers
            # until finally the greatest common divisor is found
            a = b
            b = remainder
        return a


# Example usage
if __name__ == "__main__":
    euclidean_algo = EuclideanAlgorithm()
    num1 = 36
    num2 = 48
    result = euclidean_algo.gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")