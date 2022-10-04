def symma(x):
    y = int(x)

    if (int(y / 100000) % 10) == 1:
        u = 'сто'
    elif (int(y / 100000) % 10) == 2:
        u = 'двести'
    elif (int(y / 100000) % 10) == 3:
        u = 'триста'
    elif (int(y / 100000) % 10) == 4:
        u = 'четыреста'
    elif (int(y / 100000) % 10) == 5:
        u = 'пятьсот'
    elif (int(y / 100000) % 10) == 6:
        u = 'шестьсот'
    elif (int(y / 100000) % 10) == 7:
        u = 'семьсот'
    elif (int(y / 100000) % 10) == 8:
        u = 'восемьсот'
    elif (int(y / 100000) % 10) == 9:
        u = 'девятьсот'
    elif (int(y / 100000) % 10) == 0:
        u = ''

    if int(y / 10000) % 10 == 1:
        if int(y / 1000) % 10 == 0:
            i = 'десять'
        elif int(y / 1000) % 10 == 1:
            i = 'одиннадцать'
        elif int(y / 1000) % 10 == 2:
            i = 'двенадцать'
        elif int(y / 1000) % 10 == 3:
            i = 'тринадцать'
        elif int(y / 1000) % 10 == 4:
            i = 'четырнадцать'
        elif int(y / 1000) % 10 == 5:
            i = 'пятнадцать'
        elif int(y / 1000) % 10 == 6:
            i = 'шестнадцать'
        elif int(y / 1000) % 10 == 7:
            i = 'семнадцать'
        elif int(y / 1000) % 10 == 8:
            i = 'восемнадцать'
        elif int(y / 1000) % 10 == 9:
            i = 'девятнадцать'

    elif int(y / 10000) % 10 == 2:
        i = 'двадцать'
    elif int(y / 10000) % 10 == 3:
        i = 'тридцать'
    elif int(y / 10000) % 10 == 4:
        i = 'сорок'
    elif int(y / 10000) % 10 == 5:
        i = 'пятьдесят'
    elif int(y / 10000) % 10 == 6:
        i = 'шестьдесят'
    elif int(y / 10000) % 10 == 7:
        i = 'семьдесят'
    elif int(y / 10000) % 10 == 8:
        i = 'восемьдесят'
    elif int(y / 10000) % 10 == 9:
        i = 'девяноста'
    elif int(y / 10000) % 10 == 0:
        i = ''

    if (int(y / 10000) % 10) != 1:
        if (int(y / 1000) % 10) == 1:
            r = 'одна тысяча'
        elif (int(y / 1000) % 10) == 2:
            r = 'две тысячи'
        elif (int(y / 1000) % 10) == 3:
            r = 'три тысячи'
        elif (int(y / 1000) % 10) == 4:
            r = 'четыре тысячи'
        elif (int(y / 1000) % 10) == 5:
            r = 'пять тысяч'
        elif (int(y / 1000) % 10) == 6:
            r = 'шесть тысяч'
        elif (int(y / 1000) % 10) == 7:
            r = 'семь тысяч'
        elif (int(y / 1000) % 10) == 8:
            r = 'восемь тысяч'
        elif (int(y / 1000) % 10) == 9:
            r = 'девять тысяч'
        elif (int(y / 1000) % 10) == 0:
            r = ''

    if (int(y / 100) % 10) == 1:
        h = 'сто'
    elif (int(y / 100) % 10) == 2:
        h = 'двести'
    elif (int(y / 100) % 10) == 3:
        h = 'триста'
    elif (int(y / 100) % 10) == 4:
        h = 'четыреста'
    elif (int(y / 100) % 10) == 5:
        h = 'пятьсот'
    elif (int(y / 100) % 10) == 6:
        h = 'шестьсот'
    elif (int(y / 100) % 10) == 7:
        h = 'семьсот'
    elif (int(y / 100) % 10) == 8:
        h = 'восемьсот'
    elif (int(y / 100) % 10) == 9:
        h = 'девятьсот'
    elif (int(y / 100) % 10) == 0:
        h = ''

    if int(y / 10) % 10 == 1:
        if (y % 10) == 0:
            m = 'десять'
        elif (y % 10) == 1:
            m = 'одиннадцать'
        elif (y % 10) == 2:
            m = 'двенадцать'
        elif (y % 10) == 3:
            m = 'тринадцать'
        elif (y % 10) == 4:
            m = 'четырнадцать'
        elif (y % 10) == 5:
            m = 'пятнадцать'
        elif (y % 10) == 6:
            m = 'шестнадцать'
        elif (y % 10) == 7:
            m = 'семнадцать'
        elif (y % 10) == 8:
            m = 'восемнадцать'
        elif (y % 10) == 9:
            m = 'девятнадцать'

    elif int(y / 10) % 10 == 2:
        m = 'двадцать'
    elif int(y / 10) % 10 == 3:
        m = 'тридцать'
    elif int(y / 10) % 10 == 4:
        m = 'сорок'
    elif int(y / 10) % 10 == 5:
        m = 'пятьдесят'
    elif int(y / 10) % 10 == 6:
        m = 'шестьдесят'
    elif int(y / 10) % 10 == 7:
        m = 'семьдесят'
    elif int(y / 10) % 10 == 8:
        m = 'восемьдесят'
    elif int(y / 10) % 10 == 9:
        m = 'девяноста'
    elif int(y / 10) % 10 == 0:
        m = ''

    if (int(y / 10) % 10) != 1:
        if (y % 10) == 1:
            l = 'один рубль'
        elif (y % 10) == 2:
            l = 'два рубля'
        elif (y % 10) == 3:
            l = 'три рубля'
        elif (y % 10) == 4:
            l = 'четыре рубля'
        elif (y % 10) == 5:
            l = 'пять рублей'
        elif (y % 10) == 6:
            l = 'шесть рублей'
        elif (y % 10) == 7:
            l = 'семь рублей'
        elif (y % 10) == 8:
            l = 'восемь рублей'
        elif (y % 10) == 9:
            l = 'девять рублей'
        elif (y % 10) == 0:
            l = ''

    w = ''
    if int(y // 10000) >= 1 == 0:
        w = 'тысяч'

    p = ''
    if int(y % 10) == 0:
        p = 'рублей'

    print(f' Сумма : {u} {i} {r} {w} {h} {m} {l} {p}')


def keys1(s, value):
    for k, v in s.items():
        if v == value:
            return k











