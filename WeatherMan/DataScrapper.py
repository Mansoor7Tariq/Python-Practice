
def find_index_of_field(field_name, search_list):
    for sublist in search_list:
        if sublist:
            for fn in range(len(sublist)):
                if sublist[fn].strip() == field_name:
                    return fn
    return None


def Scrap_data_from_field(field_name, fileData):
    index = find_index_of_field(field_name, fileData)

    if index is None:
        index = 0

    start_index = 1 if fileData[0] != [] else 2
    data_list = []

    for row in fileData[start_index:]:
        data_list.append(row[index])

    return data_list
