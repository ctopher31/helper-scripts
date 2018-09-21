#!/usr/bin/env python3
import os, glob

#
# Changes the file extensions of files in a directory
#
# param1: path to directory
# param2: glob for files to remove
#
def delete_files_recursively(path, file_glob):
    for filename in glob.iglob(os.path.join(path, file_glob), recursive=True):
        os.remove(os.path.join(path, filename))

if __name__ == '__main__':
    import sys
    delete_files_recursively(sys.argv[1], sys.argv[2])
