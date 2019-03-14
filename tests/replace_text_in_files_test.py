# replace_text_in_files_test.py
import sys, glob, os
import pytest

sys.path.append('../')

from replace_text_in_files import replace_text_in_files

path_file_glob = os.path.join(os.getcwd(), 'test-text-file.txt')

def test_replace_text_in_files():
    replace_text_in_files(path_file_glob, 'consectetur', 'Chris')

    for filename in glob.iglob(path_file_glob, recursive=True):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                print(str(index) + ' ' + line)
                assert 'consectetur' not in line
                assert 'Chris' in line
