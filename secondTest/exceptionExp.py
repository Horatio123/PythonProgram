a = 3
b = 0

# try:
#     res = a / b
# except Exception as e:
#     print("Error is: ", e, type(e))

try:
    res = a / b
except TypeError as e:
    print("Error is: ", type(e))
except ZeroDivisionError as e:
    print("Error is: ", type(e))
else:
    print(res)
finally:
    print("final step")


# class Water:
#     def __init__(self, tmp):
#         self.tmp = tmp
#
#     def drink_water(self):
#         if self.tmp > 85:
#             raise Exception("water too hot")
#         elif self.tmp < 65:
#             raise ValueError("water low temperature")
#         else:
#             print("it is time to drink water")

class TmpTooHot(Exception):
    def __init__(self, msg):
        super().__init__(msg)


# notice super()
class TmpTooLow(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Water:
    def __init__(self, tmp):
        self.tmp = tmp

    def drink_water(self):
        if self.tmp > 85:
            raise TmpTooHot("water too hot: " + str(self.tmp))
        elif self.tmp < 65:
            raise TmpTooLow("water low temperature: " + str(self.tmp))
        else:
            print("it is time to drink water")


water = Water(64)
water.drink_water()
