#!/usr/bin/env python
# coding: utf-8

# @Time    : 2019/4/9 16:38
# @Author  : Yuang
# @Email   : catyuang@gmail.com
# @File    : add_quotes.py
# @Software: PyCharm
# @Function: 给行以特定分割符分割的文件添加引号，例如 lastEndDate: 2019-04-13 00:00:00 ==> 'lastEndDate': '2019-04-13 00:00:00'


def add_quotes(source, target, sep):
    with open(source, 'r', encoding='utf8') as source_file:
        with open(target, 'w', encoding='utf8') as target_file:
            lines = source_file.readlines()
            
            for line in lines:
                line_tup = line.split(sep, 1)
                right = line_tup[1].replace('\n', '').strip() if len(line_tup) > 1 else "''"
                left = line_tup[0].strip()
                
                target_file.writelines('{left!r}: {right!r},\n'.format_map({'left': left, 'right': right}))


if __name__ == '__main__':
    add_quotes('a_raw.txt', 'a_new.txt', ':')
