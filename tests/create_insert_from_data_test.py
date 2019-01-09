# create_insert_from_data_test
import sys
import pytest, os

sys.path.append('../')

from create_insert_from_data import create_insert_from_data

fullpath_filename = os.path.join(os.getcwd(), 'test-data.sql')
table_name = 'dbo.SwatchesToCategories'
delimiter = '    '
new_delimiter = ', '
values = 'Id,Name,ProductLineId'
column_types = 'int,string,string,string,string,string,int'

def test_create_insert_from_data():
    create_insert_from_data(fullpath_filename, table_name, values, delimiter, new_delimiter, column_types)

    created_file = open(os.path.join(os.getcwd(), 'test-data-formatted.sql'), 'r')
    lines = created_file.readlines()
    for index, line in enumerate(lines):
        split_line = line.split(', ')
        if index == 0:
            assert line in 'INSERT INTO dbo.SwatchesToCategories (Id,Name,ProductLineId)\n'
        elif index == 1:
            assert line == 'VALUES\n'
        elif index == 2:
            assert line == '''(39, '03', 'Spectrum', 'Very White', '0801', '03B0801.jpg', NULL),\n'''
            assert split_line[0] == '(39'
            assert split_line[1] == "'03'"
            assert split_line[2] == "'Spectrum'"
            assert split_line[3] == "'Very White'"
        elif index == 3:
            assert line == "(993, '14', '<span class=\\'green\\'>&Dagger;</span>Prospect', 'Chestnut', 'V2429', '14BV2429.jpg', NULL),\n"
        elif index == 4:
            assert line == "(1098, '16', 'Retro', 'Robin\\'s Egg', 'T2004', '14B32004.jpg', NULL),\n"
        elif index == 5:
            assert line == '''(17004, '09', 'Cornices - Shown in Creampuff', '5 1/2\\" Marquee', '1603', 'wood_marquee_5p5in_cornice.jpg', 0);\n'''

    created_file.close()
