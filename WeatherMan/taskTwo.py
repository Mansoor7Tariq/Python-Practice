from DataScrapper import Scrap_data_from_field
from HelpingFunctions import convert_str_list_to_int, convert_simple_date_to_full_date


def taskTwo(file_data):

    # -------- AVERAGE MAXIMUM TEPERATURE

    avg_max_temp = 0

    avg_max_temp_list = Scrap_data_from_field(
        'Mean TemperatureC', file_data[0])
    avg_max_temp_date_list = Scrap_data_from_field(
        'PKT', file_data[0])
    avg_max_temp_list = convert_str_list_to_int(avg_max_temp_list)
    if (avg_max_temp < max(avg_max_temp_list)):
        avg_max_temp = max(avg_max_temp_list)
        avg_max_temp_date = avg_max_temp_date_list[avg_max_temp_list.index(
            avg_max_temp)]

    print(
        f'Highest Average: {avg_max_temp}C on {convert_simple_date_to_full_date(avg_max_temp_date)}')

    # -------- AVERAGE MINIMUM TEPERATURE

    avg_min_temp = 999
    avg_min_temp_list = Scrap_data_from_field(
        'Mean TemperatureC', file_data[0])
    avg_min_temp_date_list = Scrap_data_from_field(
        'PKT', file_data[0])
    avg_min_temp_list = convert_str_list_to_int(avg_min_temp_list)
    if (avg_min_temp > min(avg_min_temp_list)):
        avg_min_temp = min(avg_min_temp_list)
        avg_min_temp_date = avg_min_temp_date_list[avg_min_temp_list.index(
            avg_min_temp)]

    print(
        f'Lowest Average: {avg_min_temp}C on {convert_simple_date_to_full_date(avg_min_temp_date)}')

    # -------- AVERAGE HUMID TEPERATURE

    avg_humid_temp = 0
    avg_humid_temp_list = Scrap_data_from_field(
        'Mean Humidity', file_data[0])
    avg_humid_temp_date_list = Scrap_data_from_field(
        'PKT', file_data[0])
    avg_humid_temp_list = convert_str_list_to_int(avg_humid_temp_list)
    if (avg_humid_temp < max(avg_humid_temp_list)):
        avg_humid_temp = max(avg_humid_temp_list)
        avg_humid_temp_date = avg_humid_temp_date_list[avg_humid_temp_list.index(
            avg_humid_temp)]

    print(
        f'Average Humid: {avg_humid_temp}C on {convert_simple_date_to_full_date(avg_humid_temp_date)}')
