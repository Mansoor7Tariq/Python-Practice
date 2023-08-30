import calendar


def convert_str_list_to_int(list):
    return [int(x) if x != '' else 0 for x in list]


def convert_simple_date_to_full_date(date):
    date = date.split('-')
    month_name = calendar.month_name[int(date[1])]
    return (f'{month_name} {date[2]} ')


def remove_garbage_from_file(data):
    if '<' in data[-1][0]:
        data.pop()


def check_input_arguments(flag, date):
    if (flag != '-a' and flag != '-b' and flag != '-c' and flag != '-d'):
        print('Invalid Flag')
        return False
    if flag == '-a' and '/' in date:
        print('Wrong Date Formate According To The Flag')
        return False
    if (flag == '-b' or flag == '-c' or flag == '-d') and '/' not in date:
        print('Wrong Date Formate According To The Flag')
        return False
    return True
