# rename_extensions_test.py
import os, sys
import pytest

sys.path.append('../')

from rename_extensions import rename_extensions
from test_utils import set_up_directories_files, tear_down_directories_files

path = os.path.join(os.getcwd(), 'foo')

def test_rename_extensions():
    set_up_directories_files(path)
    rename_extensions(path, '**/*.test', '.txt')

    for root, dirs, files in os.walk(path):
        print(f'Directory: {root}')

        for file in files:
            print(f'\tFile: {file}')

        assert os.path.isfile(os.path.join(root, 'foo.txt')) == True
        assert os.path.isfile(os.path.join(root, 'bar.txt')) == True
        assert os.path.isfile(os.path.join(root, 'foo.test')) == False
        assert os.path.isfile(os.path.join(root, 'bar.test')) == False

    tear_down_directories_files(path)
