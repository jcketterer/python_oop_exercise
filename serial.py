"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = self.next = start

    def __repr__(self):
        return f"SerialGenerator(Start={self.start} Next={self.next + 1})"

    def generate(self):
        self.next += 1
        return self.next - 1

    ##^^^ the -1 is to start at the number that was originally decided then add one. Instead of starting at 101 right away we start at 100 then 101 ( 101-1 = 100)

    def reset(self):
        self.next = self.start
