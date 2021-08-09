#! -*- coding: utf-8
import re

# エンコード宣言
encoding_declaration = r'#[\s*]-\*-[\s*]coding:[\s*][\W+][\s*]-\*-'  # エンコード宣言
encoding_declaration_on_emacs = r'#[\s*]vim:fileencoding=[\s*][\W+]'  # GNU emacs用のエンコード宣言

# 識別子(identifier)おびキーワード(keyword)
_id_start = r''
id_start = re.escape(_id_start)
_id_continue = r''
id_continue = re.escape(_id_continue)
_xid_start = r''
xid_start = re.escape(_xid_start)
_xid_continue = r''
xid_continue = re.escape(_xid_continue)
identifier = re.escape(xid_continue) + r' ' + re.escape(xid_continue) + r'*'

Lu                  = r'[A-Z]'  # 大文字(Upper letters)
Ll                  = r'[a-z]'  # 小文字(Lowwer letters)
Lt                  = r'^[A-Z]'  # 先頭が大文字(Titlecase letters)
Lm                  = r'[\W]?'  # 修飾文字(Modifier letters)  ->  いまひとつよくわかっていない
Lo                  = r'[\W]?'  # その他の文字(Other letters)  ->  いまひとつよくわかっていない
Nl                  = r'[\d]'  # 数値を表す文字(Letter numbers)
Mn                  = r'[\W]?'  # 字幅のない記号(Nonspacing marks)  ->  いまひとつよくわかっていない
Mc                  = r'[\W]?'  # 字幅のある結合記号(Spacing combining marks)  ->  いまひとつよくわかっていない
Nd                  = r'[\W]?'  # 10進数字(Decimal numbers)  ->  いまひとつよくわかっていない
Pc                  = r'[\W]?'  # 連結用句読記号(Connector punctuations)  ->  いまひとつよくわかっていない
Other_ID_Start      = r'[\W]?'  # explicit list of characters in PropList.txt to support backwards compatibility  ->  いまひとつよくわかっていない
Other_ID_Continue   = r'[\W]?'  # explicit list of characters in PropList.txt to support backwards compatibility  ->  いまひとつよくわかっていない

keywords = ['False', 'await', 'else', 'import', 'pass',
            'None', 'break', 'except', 'in', 'raise',
            'True', 'class', 'finally', 'is', 'return',
            'and', 'continue', 'for', 'lambda', 'try',
            'as', 'def', 'from', 'nonlocal', 'while'
            'assert', 'del', 'global', 'not', 'with'
            'async', 'elif', 'if', 'or', 'yield']

# 予約済みの識別子種

# 文字列及びバイト列リテラル
_stringprefix = 'r|u|R|U|f|F|fr|Fr|fR|FR|rf|rF|Rf|RF'

# stringliteral = re.escape(_stringprefix)
stringprefix = re.escape(_stringprefix)
shortstring = ''
