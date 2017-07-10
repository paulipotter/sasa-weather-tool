def to_int(list):
    return int(''.join(list))


def format_list(row):
    new_list = []
    print(row)
    date = datetime(to_int(row[1][:4]), to_int(row[1][4:6]), to_int(row[1][6:8]), to_int(row[1][8:10]), 30, 00)

    new_list.insert(0,date)

    for i in range(4,len(row)):
        if row[i] == '*':
            new_list.append(0)
        else:
            new_list.append(row[i])
            print(type(row[i]), row[i])
    return new_list
