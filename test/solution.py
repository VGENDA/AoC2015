f = open('input.txt', 'r')
inp = f.read()

out = []


def enum(inp):
    unknown = inp.count('?')  # подсчитываем количество неизвестных переменных

    # цикл, перебирающий все возможные варианты, количество которых зависит от количества неизвестных
    for i in range(0, int('9' * unknown)):
        i = str(i).zfill(unknown)
        q = -1
        res_string = ''
        for j in inp:
            if j != '?':
                res_string += j
            else:
                q += 1
                res_string += i[q]

        # разделяем числа в получившихся строках на a_n, b_n, c_n
        res = res_string.replace('=', '+')
        numbers = res.split('+')
        a_n = int(numbers[0])
        b_n = int(numbers[1])
        c_n = int(numbers[2])

        # записываем верные варианты в out
        if (a_n != 0 and b_n != 0 and c_n != 0) and a_n + b_n == c_n:
            out.append(res_string)

    # если out пуст => решений нет => impossible
    if not out:
        print('impossible')
    else:
        print(out)

        # в условии просят вывести любое из решений, но я надеюсь вывод всегда первого элемента не будет ошибкой :Р
        o = open('output.txt', 'w')
        o.write(str(out[0]))
        o.close()


enum(inp)
