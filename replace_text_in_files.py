#!/usr/bin/env python3
import glob, os, fileinput

#
# Changes the file extensions of files in a directory
#
# param1: path to directory with filename or file extension glob or filename
# param2: text to replace
# param3: replacement text
#
def replace_text_in_files(path_file_glob, text_to_search, replacement_text):
    for filename in glob.iglob(path_file_glob, recursive=True):

        # Read in the file
        with open(filename, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(text_to_search, replacement_text)

        # Write the file out again
        with open(filename, 'w') as updated_file:
            updated_file.write(filedata)

if __name__ == '__main__':
    import sys
    replace_text_in_files(sys.argv[1], sys.argv[2], sys.argv[3])
