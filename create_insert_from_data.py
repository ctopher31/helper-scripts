#!/usr/bin/env python3
import glob, os

#
# Changes the file extensions of files in a directory
#
# param1: filename with full path
#
def create_insert_from_data(fullpath_filename, table_name, values, delimiter, new_delimiter, column_types):
    column_types_list = column_types.split(',')
    path = os.path.split(os.path.abspath(fullpath_filename))[0]
    split_filename = os.path.split(os.path.abspath(fullpath_filename))[1].split('.', 1)
    stripped_fullpath_filename = os.path.join(path, split_filename[0] + '-stripped.' + split_filename[1])
    new_fullpath_filename = os.path.join(path, split_filename[0] + '-formatted.' + split_filename[1])

    stripped_file = open(stripped_fullpath_filename, 'w')
    newfile = open(new_fullpath_filename, 'w')
    newfile.write('INSERT INTO ' + table_name + ' (' + values + ')\nVALUES\n')

    file = open(fullpath_filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        if line != '':
            delimited_line = ''
            splitlines = str(line).split(delimiter)
            for item in splitlines:
                if item not in delimiter:
                    stripped_line = str(item).replace("'", "\\'").replace('"', '\\"').strip()
                    delimited_line += stripped_line + new_delimiter

            stripped_file.write(delimited_line[:-(len(new_delimiter))] + '\n')
            newline_items = delimited_line[:-(len(new_delimiter))].split(new_delimiter)
            newline = ''
            for index2, newline_item in enumerate(newline_items):
                if newline_item.lower() == 'null' or column_types_list[index2].lower() == 'int':
                    newline += newline_item + new_delimiter
                elif column_types_list[index2].lower() == 'string':
                    newline += '\'' + newline_item + '\'' + new_delimiter

            newfile.write('(' + newline[:-(len(new_delimiter))] + ')')
            newfile.write(';\n') if index == len(lines) - 1 else newfile.write(',\n')
    newfile.write('GO\n')

    file.close()
    newfile.close()

if __name__ == '__main__':
    import sys
    create_insert_from_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
