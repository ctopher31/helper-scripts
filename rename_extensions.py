#!/usr/bin/env python3
import glob, os

#
# Changes the file extensions of files in a directory
#
# param1: path to directory
# param2: extension to replace as glob
# param3: new extension
#
def rename_extensions(path, file_glob, extension):
    for filename in glob.iglob(os.path.join(path, file_glob), recursive=True):
        os.rename(filename, ''.join([filename.rsplit('.', 1)[0], extension]))

if __name__ == '__main__':
    import sys
    rename_extensions(sys.argv[1], sys.argv[2], sys.argv[3])
