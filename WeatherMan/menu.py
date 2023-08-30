
from Input import inputData
from taskOne import taskOne
from taskTwo import taskTwo
from taskThree import taskThree
from bonusTask import bonusTask
from HelpingFunctions import check_input_arguments


def menu(flag, date, location):

    file_data, file_names, condition = inputData(
        date, location)

    if (check_input_arguments(flag, date) and condition):
        if flag == '-a' and file_names:
            print('Task One')
            taskOne(file_names, file_data)
        elif flag == '-b' and file_names:
            print('Task Two')
            taskTwo(file_data)
        elif flag == '-c' and file_names:
            print('Task Three')
            taskThree(file_data)
        elif flag == '-d' and file_names:
            print('Task Bonus')
            bonusTask(file_data)
        else:
            print("Error Occured In Weather Man Project")
