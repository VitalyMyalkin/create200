from itertools import product


def create_200():
    """Выводит все возможные варианты последовательности символов.

    9876543210, операторы + или - и результат 200."""
    for item in product(possible_symbols, repeat=len(numbers) - 1):
        combine = expr % item
        if eval(combine) == 200:
            print(f'{combine}=200')


if __name__ == '__main__':
    numbers = '9876543210'
    expr = '%s'.join([str(number) for number in numbers])
    possible_symbols = ['+', '-', '']
    create_200()
