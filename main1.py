def test(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


# Пример использования функции
test(1, 2, 3, name='Nikita', age=22)


def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 2)


print(summa(14))
