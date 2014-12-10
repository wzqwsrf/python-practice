import os


def list_file(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            name
            # print os.path.join(root, name)
        for name in dirs:
            # print os.path.join(root, name)
            name

list_file('/home/zhenqingwang/git_work/acm')