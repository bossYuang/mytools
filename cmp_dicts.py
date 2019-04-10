#!/usr/bin/env python
# coding: utf-8

# @Time    : 2019/4/9 15:17
# @Author  : Yuang
# @Email   : catyuang@gmail.com
# @File    : cmp_dicts.py.py
# @Software: PyCharm
# @Function: 键值较多时，快速查找


class QueryDiffKey:
    """
        raw_paras : 基准
        create_paras : 自定义
        cmp_value_diff : 对比同key的不同的value
        value_diff : 同key不同value，只保留基准的key-value, 用于直接复制使用, 二分法查找
        raw_only : 只在基准中含有的key
        create_only : 只在自定义中含有的key
    """
    
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
    
    def open_files(self):
        self.raw_paras = open(self.file1)
        self.create_paras = open(self.file2)
        
        self.cmp_value_diff = open('-cmp_value_diff.txt', 'w', encoding='utf-8')
        self.value_diff = open('-value_diff.txt', 'w', encoding='utf-8')
        self.raw_only = open('-raw_only.txt', 'w', encoding='utf-8')
        self.create_only = open('-create_only.txt', 'w', encoding='utf-8')
    
    def query_dict(self):
        self.raw = eval(self.raw_paras.read())
        self.create = eval(self.create_paras.read())
        self.same_keys = self.raw.keys() & self.create.keys()
        self.raw_only_keys = self.raw.keys() - self.create.keys()
        self.create_only_keys = self.create.keys() - self.raw.keys()
    
    def write_to_files(self):
        for k in self.same_keys:
            if self.raw[k] != self.create[k]:
                self.cmp_value_diff.write('{k!r}: {v1!r} ==> {v2!r},\n'.format_map({'k': k, 'v1': self.raw[k], 'v2': self.create[k]}))
                self.value_diff.write('{k!r}: {v!r},\n'.format_map({'k': k, 'v': self.raw[k]}))
        
        for k in self.raw_only_keys:
            self.raw_only.write('{k!r}: {v!r},\n'.format_map({'k': k, 'v': self.raw[k]}))
        
        for k in self.create_only_keys:
            self.create_only.write('{k!r}: {v!r},\n'.format_map({'k': k, 'v': self.create[k]}))
    
    def close_files(self):
        self.raw_paras.close()
        self.create_paras.close()
        
        self.cmp_value_diff.close()
        self.value_diff.close()
        self.raw_only.close()
        self.create_only.close()


def main():
    qd = QueryDiffKey('a_raw.txt', 'a_create.txt')
    qd.open_files()
    qd.query_dict()
    qd.write_to_files()
    qd.close_files()


if __name__ == '__main__':
    main()
