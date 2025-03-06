class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"There are {self._size * '🍪'} cookies in the jar!" if self._size > 0 else "Empty jar"

    def deposit(self, n):
        if n < 0:
            raise ValueError("Number cannot be negative")
        new_size = self._size + n
        if new_size > self._capacity:
            raise ValueError("Too many cookies in the jar!")
        self._size = new_size

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Number cannot be negative")
        new_size = self._size - n
        if new_size < 0:
            raise ValueError("There are not that many cookies to take!")
        self._size = new_size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    print(str(jar))


if __name__ == '__main__':
    main()