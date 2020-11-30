from sys import argv


def sal():
    try:
        time, salary, bonus = map(float, argv[1:])
        res = time * salary + bonus
        print(f'Заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')


sal()
