from DataScrapper import Scrap_data_from_field
from HelpingFunctions import convert_str_list_to_int, convert_simple_date_to_full_date


def taskOne(file_names, file_data):

    # -------- MAXIMUM TEPERATURE

    max_temp = 0
    for index in range(0, len(file_names), 1):

        max_temp_list = Scrap_data_from_field(
            'Max TemperatureC', file_data[index])

        max_temp_date_list = Scrap_data_from_field(
            'PKT', file_data[index])

        max_temp_list = convert_str_list_to_int(max_temp_list)

        if (max_temp < max(max_temp_list)):
            max_temp = max(max_temp_list)
            max_temp_date = max_temp_date_list[max_temp_list.index(max_temp)]

    print(
        f'Highest: {max_temp}C on {convert_simple_date_to_full_date(max_temp_date)}')

    # -------- MINIMUM TEPERATURE

    min_temp = 999
    for index in range(0, len(file_names), 1):
        min_temp_list = Scrap_data_from_field(
            'Min TemperatureC', file_data[index])

        min_temp_date_list = Scrap_data_from_field(
            'PKT', file_data[index])

        min_temp_list = convert_str_list_to_int(min_temp_list)

        if (min_temp > min(min_temp_list)):
            min_temp = min(min_temp_list)
            min_temp_date = min_temp_date_list[min_temp_list.index(min_temp)]

    print(
        f'Lowest: {min_temp}C on {convert_simple_date_to_full_date(min_temp_date)}')

    # -------- MAXIMUM HUMID TEPERATURE

    max_humid_temp = 0
    for index in range(0, len(file_names), 1):
        max_humid_list = Scrap_data_from_field(
            'Max Humidity', file_data[index])

        humid_temp_date_list = Scrap_data_from_field(
            'PKT', file_data[index])

        max_humid_list = convert_str_list_to_int(max_humid_list)

        if (max_humid_temp < max(max_humid_list)):
            max_humid_temp = max(max_humid_list)
            humid_temp_date = humid_temp_date_list[max_humid_list.index(
                max_humid_temp)]

    print(
        f'Humid: {max_humid_temp}% on {convert_simple_date_to_full_date(humid_temp_date)}')
