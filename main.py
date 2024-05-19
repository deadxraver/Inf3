import task1, task2, task3
#test = task1,2 || list = task3
try:
    task_num = input('Enter number of task: ')
    if task_num == '1': task1.task1()
    elif task_num == '2': task2.task2()
    elif task_num == '3': task3.task3()
    else: exit(0)
except:
    print("Wrong input")

# Ввод в заданиях 1 и 2 (кроме тестов) реализован с использованием ввода через консоль. В задании 3 ввод реализован через
# файл, т.к. логично, что список учеников будет загружаться файлом, а также непонятно, каким образом программа будет
# понимать, на каком студенте список заканчивается, т.к. их количество может плавать