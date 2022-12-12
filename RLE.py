import re
method = int(input('Введите цифру метода: сжатие = 1 / открытие = 2 -> '))
if method == 1:
    path = 'Open.txt'
    data = open(path, 'r')
    for open_str in data:
        temp = open_str[0]
        count = 0
        my_zip = ''
        for chair in range(len(open_str)):
            if open_str[chair] == temp:
                count += 1
            else:
                my_zip += f'{count}{temp}'
                temp = open_str[chair]
                count = 1
        temp = open_str[-1]
        revers = open_str[::-1]
        count = 0
        for chair in range(len(revers)):
            if revers[chair] == temp:
                count += 1
            else:
                break
        my_zip += f'{count}{temp}'
        print(my_zip)
    data.close()
elif method == 2:
    path = 'Arhiv.txt'
    data = open(path, 'r')
    for zip_str in data:
        parts = re.findall(r'\D+|\d+', zip_str)
        count = 0
        get_open = ''
        while count < len(parts) - 1:
            my_str = int(parts[count]) * parts[count + 1]
            count += 2
            get_open += my_str
        print(get_open)
    data.close()