import codecs, re

def task3():
    myGroup = input('Enter your group(PXXXX): ')
    n = input('Number of file: ')
    with codecs.open(f'list{n}.txt', 'r', 'utf-8') as f:
        students = f.readlines()
    lettersForEach, groups = [], []
    for student in students:
        lettersForEach.append(re.findall(r'[A-ZА-Я][^0-9]', student))
        groups.extend(re.findall(r'[A-Z][0-9]+', student))
    for i, v in enumerate(students):
        if all(letter[0] == lettersForEach[i][0][0] for letter in lettersForEach[i][1:]) and groups[i] == myGroup:
            continue
        else:
            print(v, end='')

# def task3_test():
#     t = input('Enter test number (1-5): ')
#     group = input('Enter your group: ')
#     with codecs.open(f'list{t}.txt', 'r', 'utf-8') as f:
#         list = f.readlines()
#     for v in list:
#         if (v.count(v[0]) == 3 and '-' not in v or v.count(v[0]) == 4) and v.split()[-1] == group:
#             continue
#         else:
#             print(v, end='')