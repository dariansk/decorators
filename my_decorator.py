import datetime


def logger(filepath):

    def _logger(old_function):

        def new_function(*args, **kwargs):
            with open(filepath, 'a') as new_file:
                new_file.write(f'Дата и время вызова: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}\n')
                new_file.write(f'Вызвана функция: {old_function.__name__} c аргументами: {args} и {kwargs}\n')
                result = old_function(*args, **kwargs)
                new_file.write(f'Результат вызова функции: {result}\n')
                new_file.write(f'{"-"*50}\n')
            return result

        return new_function

    return _logger
