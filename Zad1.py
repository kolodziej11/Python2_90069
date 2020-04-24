from functools import update_wrapper


class MyDeco:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        return self.func(*args, **kwargs)


class MyIterator:
    def __init__(self, max_val):
        self.__current_val = 0
        self.__max_val = max_val

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.__current_val
        self.__current_val += 1

        if tmp == self.__max_val:
            print(f'Liczba wywołań funkcji: {MyIterator.fib.num_calls}')
            raise StopIteration
        return MyIterator.fib(self, self.__current_val)

    @MyDeco
    def fib(self, num):
        if num < 2:
            return num
        return MyIterator.fib(self, num - 2) + MyIterator.fib(self, num - 1)


def main():
    obj = MyIterator(15)
    it = iter(obj)

    for el in it:
        print(el)

    print(obj)


if __name__ == "__main__":
    main()