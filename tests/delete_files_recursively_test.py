# delete_files_recursively_test.py
import sys
import pytest, os

sys.path.append('../')

from delete_files_recursively import delete_files_recursively
from test_utils import set_up_directories_files, tear_down_directories_files

path = os.path.join(os.getcwd(), 'foo')

def test_delete_files_recursively():
    set_up_directories_files(path)
    delete_files_recursively(path, '**/*.test')

    for root, dirs, files in os.walk(path):
        print(f'Directory: {root}')

        for file in files:
            print(f'\tFile: {file}')

        assert os.path.isfile(os.path.join(root, 'bar.txt')) == True
        assert os.path.isfile(os.path.join(root, 'foo.test')) == False

    tear_down_directories_files(path)
