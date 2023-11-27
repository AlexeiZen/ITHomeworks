while True:
    try:
        num1 = input('Введите первое число:')
        num2 = input('Введите второе число:')
        res = int(num1) / int(num2)
        break
    except ZeroDivisionError:
        print('Вы делите на ноль! Введите числа повторно!')
    except ValueError:
        print('Вы ввели не числа! Введите числа повторно!')
print(res)


