def nth_power(exponent):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of


p = nth_power(4)
del nth_power
print(p(3))
