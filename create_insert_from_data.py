#!/usr/bin/env python3
import glob, os

#
# Creates csv and sql files from raw txt file data
#
# param1: txt filename with full path
# param2: table name
# param3: comma seperated column names
# param4: delimeter to use with raw data
# param5: column types
#
def create_insert_from_data(fullpath_filename, table_name, column_names, delimiter, column_types):
    column_types_list = column_types.split(',')
    path = os.path.split(os.path.abspath(fullpath_filename))[0]
    split_filename = os.path.split(os.path.abspath(fullpath_filename))[1].split('.', 1)
    csv_fullpath_filename = os.path.join(path, split_filename[0] + '.csv')
    new_fullpath_filename = os.path.join(path, split_filename[0] + '.sql')

    csv_file = open(csv_fullpath_filename, 'w')
    sqlfile = open(new_fullpath_filename, 'w')
    sqlfile.write('INSERT INTO ' + table_name + ' (' + column_names + ')\nVALUES\n')

    file = open(fullpath_filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        if line != '':
            delimited_line = ''
            splitlines = str(line).split(delimiter)
            for item in splitlines:
                if item not in delimiter:
                    csv_line = str(item).replace("'", "\\'").replace('"', '\\"').replace('NULL', '').replace('null', '').strip()
                    delimited_line += csv_line + ','

            csv_file.write(delimited_line[:-1] + '\n')
            newline_items = delimited_line[:-1].split(',')
            newline = ''
            for index2, newline_item in enumerate(newline_items):
                if newline_item == '':
                    newline += 'NULL, '
                elif column_types_list[index2].lower() == 'int':
                    newline += newline_item + ', '
                elif column_types_list[index2].lower() == 'string':
                    newline += '\'' + newline_item + '\'' + ', '

            sqlfile.write('(' + newline[:-2] + ')')
            sqlfile.write(';\n') if index == len(lines) - 1 else sqlfile.write(',\n')
    sqlfile.write('GO\n')

    file.close()
    sqlfile.close()

if __name__ == '__main__':
    import sys
    create_insert_from_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
