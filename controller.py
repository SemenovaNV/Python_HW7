from calculation import init, sum, sub, multi, div
from logger import general_log
from view import number_type, oper, num


def launch_rocket():
    n_type, num1, num2, action = number_type()
    init(num1, num2)
    if action == '+':
        result = sum()
    elif action == '-':
        result = sub()
    elif action == '*':
        result = multi()
    elif (action == '/') and (num2 != 0):
        result = div()
    else:
        result = 'Ошибка деления на 0!'
    print(f'Результатом {oper[action]} {num[n_type]} чисел {num1} и {num2} является {result}')
    general_log(n_type, num1, num2, action, result, num)
