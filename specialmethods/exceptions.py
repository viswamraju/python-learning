"""
Any class to raise an exception should be derived from BaseException or Exception which is dervied from BaseException
"""


# class Person(Exception):
#     pass
#
# raise Person()


class CustomError(Exception):
    pass

def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError as ex:
        print(ex)
        raise CustomError("custom error") from ex


def main():
    div(10, 0)


main()
