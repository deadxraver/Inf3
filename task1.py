import re, codecs
def task1():
    isu = int(input('Enter your ISU: '))
    smile = ':;X8=['[isu % 6] + ['-', '<', '-{', '<{'][isu % 4] + '()O|\\/P'[isu % 7]
    print(f'Your smile is {smile}')
    method = input('Type r to use regex, type any other letter to use standart method: ')
    if method == 'r':
        line = input('Enter line (type /test and add its number to run test): ')
        if '/test' not in line:
            reg = r''
            for v in smile:
                reg += '[' + (v in '[]') * '\\' + v + ']'
            print(f'Number o\'smiles: {len(re.findall(reg, line))}')
        else:
            with codecs.open(line[1:] + '.txt', 'r', 'utf-8') as f:
                line = f.read()
            reg = r''
            for v in smile:
                reg += '[' + (v in '[]') * '\\' + v + ']'
            print('Line: ', line)
            print(f'Number o\'smiles: {len(re.findall(reg, line))}')
    else:
        line = input('Enter line (type /test and add its number to run test): ')
        if '/test' not in line:
            print('Number o\'smiles: ', line.count(smile))
        else:
            with codecs.open(line[1:] + '.txt', 'r', 'utf-8') as f:
                line = f.read()
            print('Line: ', line)
            print('Number o\'smiles: ', line.count(smile))
