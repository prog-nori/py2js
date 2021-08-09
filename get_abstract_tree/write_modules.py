import re

template = """def is{0}(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.{0}):
        output_dict['{0}'] = {{
{1}
        }}
    # return output_dict
"""

opt_template = """\t\t\t\t'{0}': parse_nodes(nodes.{0}, nest),"""

def tidy(s):
    s = re.sub(r'[a-z]*\s=\s', '', s)
    s = re.sub(r'[\t|\s]+\|', '', s)
    s = re.sub(r'^\s', '', s)
    s = s.replace('\n', '')
    return s

def _parse(s):
    splitted_value = s.split('(')
    func_name = ''
    tail = ''
    if len(splitted_value) >= 2:
        func_name, tail = splitted_value
        tail.replace(')', '')
        tail = tail[:-1].split(', ')
    else:
        func_name = splitted_value[0]
        tail = ''
    args = [re.sub(r'[a-z]+[\*|\?]?\s', '', x) for x in tail]
    return toUpperCammelCase(func_name), args or []

def toSnakeCase(s: str):
    return s.lower().replace(' ', '_')

def toUpperCammelCase(s: str):
    return s.replace(' ', '')

def main(args):
    with open(args[0]) as fp:
        for i in fp.readlines():
            i = tidy(i)
            func_name, arguments = _parse(i)
            options = [opt_template.format(toSnakeCase(x)) for x in list(arguments)]
            define = template.format(func_name, '\n'.join(options))
            print(define)
    return

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])