print('Hello Mars')

try:
    with open('./mission_computer_main.log', 'r', encoding='UTF-8',) as file:
        logList = file.readlines()

    for log in logList:
        print(log, end='')

    print('\n------------------')

    logList.reverse()

    for log in logList:
        print(log, end='')


except Exception as e:
    error_message = str(e)
    with open('./error_file.txt', 'w') as error_file:
        error_file.write(error_message)
    