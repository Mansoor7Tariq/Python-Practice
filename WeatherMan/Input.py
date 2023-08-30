
import calendar
import csv
import glob
from HelpingFunctions import remove_garbage_from_file

def inputData(date, location):

    location = location.lower()
    location_mappings = {
        "murree": "Murree_weather",
        "lahore": "lahore_weather",
        "dubai": "Dubai_weather"
    }

    if location not in location_mappings:
        print("Invalid Location:", location)
        return [], 0 , False

    folder_name = location_mappings[location]
    file_names=[]
    
    if ('/' in date):
        file_names.append(f"{folder_name}/{folder_name}_{date.split('/')[0]}_{calendar.month_abbr[int(date.split('/')[1])]}.txt")

    else:
        file_pattern = f"{folder_name}/{folder_name}_{date}*.txt"
        file_names = glob.glob(file_pattern)

    file_data = []

    for file_name in file_names:
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            file_data.append(list(csv_reader))

    for i in range(0, len(file_data), 1):
        remove_garbage_from_file(file_data[i])

    return file_data, file_names, True
