from capitalize import capitalize

if capitalize('hello') != 'hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
