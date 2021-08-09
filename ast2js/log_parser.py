#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

def read_file(args):
    try:
        with open(args[0]) as fp:
            lines = fp.readlines()
            return lines
    except Exception as e:
        print(e)
        exit()

def main(args):
    lines = read_file(args)
    res = ''
    indent = 0
    isSkip = False
    setIndent = lambda idt, aString: '{}{}'.format(''.join([' ' for _ in range(idt * 4)]), aString)
    f = False
    for aLine in lines:
        tmp_line = ''
        for i, aString in enumerate(aLine):
            if isSkip or aString == '\n':
                isSkip = False
                continue
            isNotLast = i < len(aLine) - 1
            next = aLine[i + 1] if isNotLast else ''
            end = ',\n' if next == ',' else '\n'
            fmt = lambda aString: '{}{}'.format(aString, end)
            if aString in ['{', '[']:
                if aString == '{' and next == '}':
                    aString = '{}'
                    isSkip = True
                if aString == '[' and next == ']':
                    aString = '{}'
                    isSkip = True
                anotherString = '{}\n'.format(aString)
                if f is True:
                    tmp_line += setIndent(indent, anotherString)
                else:
                    tmp_line += anotherString
                f = True
                indent += 1

            elif aString == ',':
                continue

            elif aString in ['}', ']']:
                anotherString = '{}\n'.format(aString)
                indent -= 1
                if i < len(aLine):
                    tmp_line += setIndent(indent, fmt(aString))
                else:
                    tmp_line += anotherString
                f = True

            elif aString == ' ':
                continue

            else:
                if f is True:
                    tmp_line += setIndent(indent, aString)
                else:
                    tmp_line += aString
                if next == ',':
                    fmt('')
                f = False
            if not aLine[i] in ['', ' ', '\n'] and len(aLine) - 1 == i:
                if aString not in ['{', '[', '}', ']', ',']:
                    tmp_line += '\n'
        print(tmp_line)
        res += tmp_line

    return

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])