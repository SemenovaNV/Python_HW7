from datetime import datetime as dt

def general_log(n_type, num1, num2, func, res, num):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'Время: {time}, Работа с {num[n_type]} числами, Число первое = {num1}, Число второе = {num2}, операция {func}, Результат = {res} \n')
