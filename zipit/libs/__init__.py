# !/usr/bin/env python
# coding: utf-8
import os
import re
import subprocess


def search_files(path, filter_dirname_list=None, filter_filename_list=None):
    """
    遍历 log_path　目录下的所有文件，并根据filer_dirname与filter_filename　过滤出符合的文件

    >>> list(os.walk('../test_data/spider'))
    [('../test_data/spider', ['teddywalker', 'huskywalker'], []), ('../test_data/spider/teddywalker', [], ['ZY00983']), ('../test_data/spider/huskywalker', [], ['RL0012', 'RL0066', 'YH0082'])]
    >>> FileIO.search_files('../test_data/spider',['teddywalker','huskywalker'],['RL','ZY'])
    ['../test_data/spider/teddywalker/ZY00983', '../test_data/spider/huskywalker/RL0012', '../test_data/spider/huskywalker/RL0066']
    >>> FileIO.search_files('../test_data/spider', ['teddywalker', 'huskywalker'], [''])
    ['../test_data/spider/teddywalker/ZY00983', '../test_data/spider/huskywalker/RL0012', '../test_data/spider/huskywalker/RL0066', '../test_data/spider/huskywalker/YH0082']
    >>> FileIO.search_files('../test_data/spider', [''], [''])
    ['../test_data/spider/teddywalker/ZY00983', '../test_data/spider/huskywalker/RL0012', '../test_data/spider/huskywalker/RL0066', '../test_data/spider/huskywalker/YH0082']

    你也可以使用正则，如，搜索目录下所有目录以walker结尾，文件以Ｒ开头并且以数字结尾的文件
    >>> FileIO.search_files('../test_data/spider', ['walker$'], ['R.*?\d+$'])
    ['../test_data/spider/huskywalker/RL0012', '../test_data/spider/huskywalker/RL0066']

    :param log_path:                    string
    :param filter_dirname_list:         list
    :param filter_filename_list:        list
    :return:                            list
    """
    file_walker = os.walk(path)

    filter_dirname_list = [] if filter_dirname_list is None else filter_dirname_list
    filter_filename_list = [] if filter_filename_list is None else filter_filename_list

    file_list = []
    for item in file_walker:
        # 如果存在文件
        if item[0] and item[2]:
            filtered = True
            dir_name = item[0].replace(path, '')

            for filter_dirname in filter_dirname_list:
                if re.search(filter_dirname, dir_name):
                    filtered = False
                    break

            if not filtered:
                for each_file in item[2]:
                    for filter_filename in filter_filename_list:
                        if re.search(filter_filename, each_file):
                            file_list.append(os.path.join(item[0], each_file))
    return file_list


def search_dir(path, filter_dirname_list=None):
    """返回相对path的文件夹路径"""
    filter_dirname_list = [] if filter_dirname_list is None else filter_dirname_list

    result = []
    if filter_dirname_list:
        for each_dir in os.listdir(path):
            filtered = False
            for filter_dirname in filter_dirname_list:
                if re.search(filter_dirname, each_dir):
                    filtered = True
                    break
            if filtered:
                result.append(each_dir)

        return result
    else:
        return list(os.listdir(path))


def run_command(command):
    # fh = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    # return list(fh.stdout.readlines())

    f=os.popen(command)
    return f.read()
