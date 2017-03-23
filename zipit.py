# !/usr/bin/env python
# coding: utf-8
from zipit.libs import *
from zipit.setting import *
import datetime


def start_zip(absolute_dir):
    print('Start zip {}'.format(absolute_dir))
    output = run_command('7za a -r {} {}'.format(absolute_dir, absolute_dir))
    if 'Everything is Ok' in output:
        print('Zipped! Start to delete.')
        run_command('rm -rf {}'.format(absolute_dir))
    else:
        print('Zip failed!')
        print(output)


def zip_dir(path, filter_dirname_list=None):
    all_dir = search_dir(path, filter_dirname_list)
    now_date = datetime.datetime.now().date()

    for each_dir in all_dir:
        dir_date = datetime.datetime.strptime(each_dir, "%Y-%m-%d").date()
        if now_date < dir_date:
            absolute_dir = os.path.join(path, each_dir)
            start_zip(absolute_dir)


if __name__ == '__main__':
    for each in TARGET_DIR:
        zip_dir(each)