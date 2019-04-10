#!/usr/bin/env python
# coding: utf-8

# @Time    : 2019/4/9 17:49
# @Author  : Yuang
# @Email   : catyuang@gmail.com
# @File    : session_headers.py
# @Software: PyCharm
# @Function: 格式化从浏览器复制出来的Request Headers -> session.headers['Content-Type'] = 'application/x-www-form-urlencoded'


def session_headers_formatter(source, target):
    with open(source, 'r', encoding='utf8') as source_file:
        with open(target, 'w', encoding='utf8') as target_file:
            lines = source_file.readlines()
            
            for line in lines:
                line_tup = line.split(': ')
                value = line_tup[1].replace('\n', '').strip() if len(line_tup) > 1 else "''"
                new_line = 'session.headers[{k!r}] = {v!r}'.format_map({'k': line_tup[0], 'v': value})
                target_file.writelines(new_line + '\n')


if __name__ == '__main__':
    session_headers_formatter('raw_headers.txt', 'new_headers.txt')
