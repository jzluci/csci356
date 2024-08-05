class Fraction:
    def __init__(self, top, bottom):
        # Initialize the fraction
        self.num = top
        self.den = bottom

        # Reduce the fraction to its lowest terms
        common = self.gcd(self.num, self.den)
        self.num //= common
        self.den //= common

    def __str__(self):
        return f"{self.num}/{self.den}"

    @staticmethod
    def gcd(m, n):
        while n != 0:
            m, n = n, m % n
        return m

    def get_num(self):
        # Return the numerator of the fraction.
        return self.num

    def get_den(self):
        # Return the denominator of the fraction.
        return self.den

    def __add__(self, other):
        if isinstance(other, Fraction):
            # Perform addition of two fractions
            new_num = self.num * other.get_den() + self.den * other.get_num()
            new_den = self.den * other.get_den()
        elif isinstance(other, int):
            # Convert integer to fraction and then add
            new_num = self.num + other * self.den
            new_den = self.den
        else:
            return NotImplemented

        # Return the resulting fraction, already in lowest terms
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        if isinstance(other, int):
            # Convert integer to fraction and then add
            new_num = other * self.den + self.num
            new_den = self.den
            # Return the resulting fraction, already in lowest terms
            return Fraction(new_num, new_den)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.num == other.get_num()) and (self.den == other.get_den())
        elif isinstance(other, int):
            return (self.num == other * self.den) and (self.den == 1)
        return False


def main():
    # Tests
    frac1 = Fraction(4, 8)  # This will be reduced to 1/2
    frac2 = Fraction(1, 2)
    result = frac1 + frac2  # Result will be 1/1, which is simplified
    frac3 = Fraction(1, 2)
    integer = 3

    # Adding reduced fraction with fraction
    print(f"{frac1} + {frac2} = {result}")

    # Equality check
    print(f"{frac1} == {frac2} is {frac1 == frac2}")

    # Adding fraction and integer
    print(f"{frac3} + {integer} = {frac3 + integer}")

    # Adding integer and fraction
    print(f"{integer} + {frac3} = {integer + frac3}")


if __name__ == '__main__':
    main()
