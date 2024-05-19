import re, codecs

def task2():
    method = input('Type r to use regex, type any other letter to use standart method: ')
    if method == 'r':
        line = input('Enter line (type /test and add its number to run test): ')
        if '/test' not in line:
            s, n = (' ' + input('Enter text: ').replace(' ', ' _ ') + ' ').split('_'), 0
            print('Suitable words are: ')
            for i in range(len(s) - 1):
                if re.search(
                        r'[^уеыаоэяиюёУЕЫАОЭЯИЮЁeuioaEUIOA][уеыаоэяиюёУЕЫАОЭЯИЮЁeuioaEUIOA]{2}[^уеыаоэяиюёУЕЫАОЭЯИЮЁeuioaEUIOA]',
                        s[i]) and len(re.findall(r'[qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNMйцкнгшщзхфвпрлджчсмтбЙЦКНГШЩЗХФВПРЛДЖЧСМТБ]', s[i + 1])) <= 3:
                    if n:
                        print(', ' + s[i].replace(' ', ''), end='')
                    else:
                        print(s[i].replace(' ', ''), end='')
                    n += 1
            if not n:
                print('No such words')
            else:
                print()
        else:
            with codecs.open(line[1:] + '.txt', 'r', 'utf-8') as f:
                line = f.read()
            s, n = (' ' + line.replace(' ', ' _ ') + ' ').split('_'), 0
            print('Suitable words are: ')
            for i in range(len(s) - 1):
                if re.search(
                        r'[^уеыаоэяиюёУЕЫАОЭЯИЮЁeuioaEUIOA][уеыаоэяиюёУЕЫАОЭЯИЮЁeuioaEUIOA]{2}[^уеыаоэяиюёУЕЫАОЭЯИЮЁeuioaEUIOA]',
                        s[i]) and len(re.findall(r'[qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNMйцкнгшщзхфвпрлджчсмтбЙЦКНГШЩЗХФВПРЛДЖЧСМТБ]', s[i + 1])) <= 3:
                    if n:
                        print(', ' + s[i].replace(' ', ''), end='')
                    else:
                        print(s[i].replace(' ', ''), end='')
                    n += 1
            if not n:
                print('No such words')
            else:
                print()
    else:
        line = input('Enter line (type /test and add its number to run test): ')
        if '/test' not in line:
            line1 = line
            for u in 'уеыаоэяиюёУЕЫАОЭЯИЮЁeuioaEUIOA':
                line1 = line1.replace(u, '*')
            line1 = line1.replace('**', '+').replace('+*', '-').replace('*+', '-').replace('++', '-').replace('+-', '-')
            line1, line = line1.split(), line.split()
            line1.append('')
            for i in range(len(line1) - 1):
                if '+' in line1[i] and len(line1[i + 1]) - sum(
                        line1[i + 1].count(k) for k in '*-+,?!:;\\|\'\"./{}[]_=@#$%^()№~`') <= 3 and i != len(line1) - 2:
                    print(line[i], end=' ')
        else:
            with codecs.open(line[1:] + '.txt', 'r', 'utf-8') as f:
                line = f.read()
            line1 = line
            for u in 'уеыаоэяиюёУЕЫАОЭЯИЮЁeuioaEUIOA':
                line1 = line1.replace(u, '*')
            line1 = line1.replace('**', '+').replace('+*', '-').replace('*+', '-').replace('++', '-').replace('+-', '-')
            line1, line = line1.split(), line.split()
            line1.append('')
            for i in range(len(line1) - 1):
                if '+' in line1[i] and len(line1[i + 1]) - sum(
                        line1[i + 1].count(k) for k in '*-+,?!:;\\|\'\"./{}[]_=@#$%^()№~`') <= 3 and i != len(line1) - 2:
                    print(line[i], end=' ')