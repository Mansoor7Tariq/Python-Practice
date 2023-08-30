from DataScrapper import Scrap_data_from_field


def taskThree(file_data):

    end = 2 if file_data[0][0] == [] else 1

    for date in range(len(file_data[0]) - end):

        max_temp_list = Scrap_data_from_field(
            'Max TemperatureC', file_data[0])

        min_temp_list = Scrap_data_from_field(
            'Min TemperatureC', file_data[0])

        print(f'{date}', end=' ')
        print('\033[31m+\033[0m' * int(max_temp_list[date]),
              f'{max_temp_list[date]}C')

        print(f'{date}', end=' ')
        print('\033[34m+\033[0m' * int(min_temp_list[date]),
              f'{min_temp_list[date]}C')
