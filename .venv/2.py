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
        return a #b=0,a is GCD


# Example usage
if __name__ == "__main__":
    euclidean_algo = EuclideanAlgorithm()

    # Accept input numbers from the user
    try:
        num1 = int(input("Enter the first positive integer: "))#gain a value
        num2 = int(input("Enter the second positive integer: "))#gain b value
        if num1 <= 0 or num2 <= 0:
            raise ValueError("Please confirm both numbers should be positive integers.")
    except ValueError as e:
        print("Invalid input: ", e)
    else:
        result = euclidean_algo.gcd(num1, num2)
        print(f"The GCD of {num1} and {num2} is: {result}")