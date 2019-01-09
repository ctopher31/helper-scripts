#!/usr/bin/env python3
import glob, os

#
# Changes the file extensions of files in a directory
#
# param1: filename with full path
#
def replace_whitespace_with_delimeter(fullpath_filename, delimiter, new_delimiter):
    path = os.path.split(os.path.abspath(fullpath_filename))[0]
    split_filename = os.path.split(os.path.abspath(fullpath_filename))[1].split('.', 1)
    new_fullpath_filename = os.path.join(path, split_filename[0] + '-stripped.' + split_filename[1])
    newfile = open(new_fullpath_filename, 'w')

    file = open(fullpath_filename, 'r')
    lines = file.readlines()
    for index, line in enumerate(lines):
        newline = ''
        if line != '':
            splitlines = str(line).split(delimiter)
            for index, item in enumerate(splitlines):
                if item not in delimiter:
                    newline += item.strip() + new_delimiter

        newfile.write(newline[:-(len(new_delimiter))] + '\n')

    file.close()
    newfile.close()

    # file2 = open(fullpath_filename, 'w')
    # newfile2 = open(new_fullpath_filename, 'r')
    # lines2 = newfile2.readlines()
    # for index, line in enumerate(lines2):
    #     if line != '':
    #         file2.write(line)
    #
    # file2.close()
    # newfile2.close()
    # newfile2.delete()

if __name__ == '__main__':
    import sys
    replace_whitespace_with_delimeter(sys.argv[1], sys.argv[2], sys.argv[3])
